from track import track
import numpy as np
import matplotlib.pyplot as plt
import sys
import race

def simulate():
    for i in xrange(10):
        print
        print "CAR", i
        print "====="
        race.train_car()

def process():
    #[(iter, time_sum, reward_sum, ncars_finished)]
    data = np.zeros((1000, 4))
    with open('learning_curve.data', 'r') as f_in:
        for line in f_in:
            if not line:
                continue
            content = line.split()
            if not bool(content[3]):
                continue

            iter = int(content[0])
            time = int(content[1])
            reward = float(content[2])

            data[iter][0] = iter
            data[iter][1] += time
            data[iter][2] += reward
            data[iter][3] += 1

    return data[:][:3]

def plot(data):
    "data = [(iter, avg_time, avg_reward)]"
    plt.plot(data[:][0], data[:][1], label="avg time to finish")
    plt.xlabel('trial')
    plt.ylabel('time steps to finish')
    plt.title('Learning curve')
    plt.savefig('learning_curve.png', bbox_inches=0)

def main():
    simulate()
    data = process()
    print data
    plot(data)

if __name__ == "__main__":
    main()
