#!/usr/bin/env python2

import numpy as np
import matplotlib.pyplot as plt
import sys
import race
import params

def simulate():
    for i in xrange(10):
        print
        print "CAR", i+1
        print "====="
        race.train_car(save_learning_curve = True)


def process_single_curves():
    """helping function to provide data only for single learning curves"""

    data = []

    last_trial = 2000

    with open(params.FILENAME, 'r') as f_in:
        for line in f_in:
            if not line: # empty line
                continue

            # (trial, time, reward, bool_finished)
            content = line.split()

            trial = int(content[0])
            time = int(content[1])

            if trial < last_trial:
                data.append(np.zeros((1000, 2)))

            data[-1][trial, :] = [trial, time]

            last_trial = trial

    return data

def process():
    '''processes the data from the file `learning_curve.data`
    @returns array of entries like (trial, avg_time, avg_reward, n_finished)
    '''
    #[(trial, time_avg, reward_avg, ncars_finished)]
    data = np.zeros((1000, 4))

    with open(params.FILENAME, 'r') as f_in:
        for line in f_in:
            if not line: # empty line
                continue

            # (trial, time, reward, bool_finished)
            content = line.split()

            # car did not finish, skip 
            if not bool(content[3]):
                continue

            trial = int(content[0])
            time = int(content[1])
            reward = float(content[2])

            data[trial][0] = trial
            data[trial][1] += time
            data[trial][2] += reward
            data[trial][3] += 1

    # find trial indices where count is zero
    # however, whole data is array of floats, so precaution is needed and that
    # is why this hideous expression
    # np.where returns a tuple of arrays; I want only first array (hence the
    # zero index in the end)
    all_fail_indices = np.where(np.abs(data[:, 3]) <= 1e-6)[0]

    # now set some values to avoid zero division
    data[all_fail_indices, 1] = 1000
    data[all_fail_indices, 3] = 1

    # make averages
    data[:, 1] /= data[:, 3]
    data[:, 2] /= data[:, 3]

    return data

def plot_learning_curve(data, description):
    
    if not 'fname' in description:
        description['fname'] = 'curve.png'

    plt.plot(data[:, 0], data[:, 1], label= description.get('label'))
    plt.xlabel(description.get('xlabel'))
    plt.ylabel(description.get('ylabel'))
    plt.title(description.get('title'))
    plt.legend(loc = description.get('loc'))
    plt.savefig('plots/' + description['fname'], bbox_inches=0)
    plt.close()

def plot_single_curves(data):

    for k in xrange(len(data)):
        fname = 'curve_car_' + str(k) + '.png'
        label = 'a learning curve'
        plot_learning_curve(data[k], fname, label)


def main(argv):
    if len(argv) == 2 and argv[1] == "-s":
        simulate()

    data = process()

    plot_learning_curve(data, {
            'fname': 'learning_curve.png',
            'label': 'avg learning curve',
            'title': 'Learning curve',
            'loc': 'upper right',
            'xlabel': 'trial',
            'ylabel': 'time steps to finish'
        }
    )
    plot_learning_curve(data[:, (0,2)], {
            'fname': 'reward_curve.png',
            'label': 'avg reward curve',
            'title': 'Reward curve',
            'loc': 'lower right',
            'xlabel': 'trials',
            'ylabel': 'reward'
        }
    )

    # plots curves for every single car
    # this is not needed, but is here just to compare the difference between an
    # averaged curve and single car run instance
    #single_data = process_single_curves()
    #plot_single_curves(single_data)


usage = '''Usage:
python2 plot_learning_curve.py [-s]

-s perform simulation; if parameter not given, program will just plot the data
    Simulation consists of 10 runs of the learning and storing that data.
'''

if __name__ == "__main__":
    if len(sys.argv) not in [1,2]:
        print usage
        sys.exit(1)

    main(sys.argv)
