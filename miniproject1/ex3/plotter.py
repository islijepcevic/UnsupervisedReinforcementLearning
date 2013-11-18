import numpy as np
import matplotlib.pyplot as plt

counter = 0

def plot(neuron, it):

    global counter
    counter += 1

    W = neuron.getW()
    print 'iteration', it
    #print W

    plt.figure(counter)

    plt.pcolor(W)
    plt.colorbar()
    plt.title('Receptive field $W$ after ' + str(it) + ' iterations')
    #plt.show()
    while True:
        try:
            plt.savefig('simulation/img%02d.png' % counter, bbox_inches = 0)
            plt.close()
            break
        except:
            print "did not save image correctly"


def plotTheta():

    fl = open('theta.data', 'r')
    read = fl.read().split('\n')[:-1]
    fl.close()

    data = []

    for line in read:
        entry = [float(x) for x in line.split()]
        data.append(entry)

    data = np.array(data)

    plt.plot(data[:,0], data[:,1], 'b-')
    plt.title(r'Evolution of \theta over the simulation time')
    plt.xlabel('$t$')
    plt.ylabel(r'\theta')
    plt.savefig('simulation/theta.png', bbox_inches = 0)

