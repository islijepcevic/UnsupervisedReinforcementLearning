import numpy as np
import matplotlib.pyplot as plt

counter = 0

'''
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
'''


def plotInput(patch, iter, time):

    #patch.shape = 16, 16
    plt.pcolor(patch[:(31*31)].reshape(31,31))
    #plt.colorbar()
    #plt.savefig('plots/input_'+str(iter)+'_'+str(time)+'.png')
    plt.show()
   
def plotWeights(weights):

#    plt.figure(2)
#    plt.subplot(331)
    plt.pcolor(weights[0][:(31*31)].reshape(31,31))

#    plt.subplot(332)
#    plt.pcolor(weights[1][:(31*31)].reshape(31,31))
#
#    plt.subplot(333)
#    plt.pcolor(weights[2][:(31*31)].reshape(31,31))
#    
#    plt.subplot(334)
#    plt.pcolor(weights[3][:(31*31)].reshape(31,31))
#
#    plt.subplot(335)
#    plt.pcolor(weights[4][:(31*31)].reshape(31,31))
#
#    plt.subplot(336)
#    plt.pcolor(weights[5][:(31*31)].reshape(31,31))
#
#    plt.subplot(337)
#    plt.pcolor(weights[6][:(31*31)].reshape(31,31))
#
#    plt.subplot(338)
#    plt.pcolor(weights[7][:(31*31)].reshape(31,31))
#
#    plt.subplot(339)
#    plt.pcolor(weights[8][:(31*31)].reshape(31,31))
#
    plt.show()


'''
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
    plt.title(r'Evolution of $\theta$ over the simulation time')
    plt.xlabel('$t$')
    plt.ylabel(r'$\theta$')
    plt.savefig('simulation/theta.png', bbox_inches = 0)
'''

