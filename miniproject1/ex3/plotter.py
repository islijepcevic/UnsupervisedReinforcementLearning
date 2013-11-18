import numpy as np
import matplotlib.pyplot as plt

def plot(neuron, it):

    W = neuron.getW()
    print 'iteration', it
    print W

    plt.pcolor(W)
    plt.title('Receptive field $W$ after ' + str(it) + ' iterations')
    plt.show()

