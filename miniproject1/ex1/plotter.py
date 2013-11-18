import matplotlib.pyplot as plt
import numpy as np

import sys

def plot():

    fname = 'data.out'
    if len(sys.argv) > 1:
        fname = sys.argv[1]

    inStream = open(fname, 'r')
    fileData = inStream.read().split('\n')
    inStream.close()

    data = []
    for line in fileData:
        if not line:
            continue

        try:
            (z, y, it) = [float(x) for x in line.split()]
        except:
            continue

        data.append((z,y))
    data = np.array(sorted(data))

    plt.plot(data[:,0], data[:,1], 'x')
    plt.xlabel('$z$')
    plt.ylabel('$y$')
    plt.title('Firing rate as a function of probability $z$')
    plt.show()
    


if __name__ == '__main__':
    plot()
