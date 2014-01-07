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
    '''this function plots all the position weights of the neural network, and
    serves as debugging code. Put it where you need it in order to see the
    weights
    '''

    fig0 = plt.figure(90)
    plt.pcolor(weights[0][:(31*31)].reshape(31,31))
    fig0.savefig('plots/weihts0.png', bbox_inches=0)

    fig1 = plt.figure(91)
    plt.pcolor(weights[1][:(31*31)].reshape(31,31))
    fig1.savefig('plots/weihts1.png', bbox_inches=0)
    
    fig2 = plt.figure(92)
    plt.pcolor(weights[2][:(31*31)].reshape(31,31))
    fig2.savefig('plots/weihts2.png', bbox_inches=0)

    fig3 = plt.figure(93)
    plt.pcolor(weights[3][:(31*31)].reshape(31,31))
    fig3.savefig('plots/weihts3.png', bbox_inches=0)

    fig4 = plt.figure(94)
    plt.pcolor(weights[4][:(31*31)].reshape(31,31))
    fig4.savefig('plots/weihts4.png', bbox_inches=0)

    fig5 = plt.figure(95)
    plt.pcolor(weights[5][:(31*31)].reshape(31,31))
    fig5.savefig('plots/weihts5.png', bbox_inches=0)

    fig6 = plt.figure(96)
    plt.pcolor(weights[6][:(31*31)].reshape(31,31))
    fig6.savefig('plots/weihts6.png', bbox_inches=0)

    fig7 = plt.figure(97)
    plt.pcolor(weights[7][:(31*31)].reshape(31,31))
    fig7.savefig('plots/weihts7.png', bbox_inches=0)

    fig8 = plt.figure(98)
    plt.pcolor(weights[8][:(31*31)].reshape(31,31))
    fig8.savefig('plots/weihts8.png', bbox_inches=0)


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

