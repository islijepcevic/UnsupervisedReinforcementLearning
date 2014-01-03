#!/usr/bin/env python2

import numpy as np
import matplotlib.pyplot as plt
import sys
import race

def simulate():
    for i in xrange(10):
        print
        print "CAR", i+1
        print "====="
        race.train_car(save_learning_curve = True)

def process():
    '''processes the data from the file `learning_curve.data`
    @returns array of entries like (trial, avg_time, avg_reward, n_finished)
    '''
    #[(trial, time_avg, reward_avg, ncars_finished)]
    data = np.zeros((1000, 4))

    with open('learning_curve.data', 'r') as f_in:
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

def plot_learning_curve(data):
    """data = [(trial, avg_time, avg_reward, n_finished)]"""

    plt.plot(data[:][0], data[:][1], label="avg time to finish")
    plt.xlabel('trial')
    plt.ylabel('time steps to finish')
    plt.title('Learning curve')
    plt.savefig('plots/learning_curve.png', bbox_inches=0)

def main(argv):
    if len(argv) == 2 and argv[1] == "-s":
        simulate()

    data = process()

    plot_learning_curve(data)


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
