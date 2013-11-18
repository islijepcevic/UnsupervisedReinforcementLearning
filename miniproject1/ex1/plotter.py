import matplotlib.pyplot as plt
import numpy as np

import sys

def plot():

    # load filename given from console
    fname = 'data.out'
    if len(sys.argv) > 1:
        fname = sys.argv[1]

    # load data
    inStream = open(fname, 'r')
    fileData = inStream.read().split('\n')
    inStream.close()

    data = []
    for line in fileData:
        if not line: # skip empty lines
            continue

        try:
            (z, y, it) = [float(x) for x in line.split()]
        except:
            # this is for the case of 'did not converge' line
            continue

        data.append((z,y))
    data = np.array(sorted(data))

    # plot
    plt.plot(data[:,0], data[:,1], 'x')
    plt.xlabel('$z$')
    plt.ylabel('$y$')
    plt.title('Firing rate as a function of probability $z$')
    plt.show()
    


if __name__ == '__main__':
    plot()
