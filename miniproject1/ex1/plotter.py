import matplotlib.pyplot as plt
import numpy as np

import sys

def fit_exponential(t, y, C=0):
    y = y - C
    y = np.log(y)
    K, A_log = np.polyfit(t, y, 1)
    A = np.exp(A_log)
    return A, K

def exponential(data, zInterval, index):
    C = np.mean(data[-5:, 1] - 0.05)
    A, K = fit_exponential(zInterval, data[index:, 1], C)
    myexp = A * np.exp(K * zInterval) + C

    return myexp

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
    wdata = []
    thdata = []
    for line in fileData:
        if not line: # skip empty lines
            continue

        try:
            (z, y, w, theta, it) = [float(x) for x in line.split()]
        except:
            # this is for the case of 'did not converge' line
            continue

        data.append((z,y))
        wdata.append((z,w))
        thdata.append((z,theta))
    data = np.array(sorted(data))
    wdata = np.array(sorted(wdata))
    thdata = np.array(sorted(thdata))

#    # exponential          
#    index = 0
#    for z in data[:, 0]:
#        index += 1
#        if z == 0.38:
#            break
#    #zInterval = np.linspace(0.38, 0.8, len(data) - index)
#    zInterval = data[index:, 0]
#
#    curve = exponential(data, zInterval, index)



    # plot
    figY = plt.figure(1)
    plt.plot(data[:,0], data[:,1], 'x')
    #plt.plot(zInterval, curve, 'r-')
    plt.xlabel('$z$')
    plt.ylabel('$y$')
    plt.title('Firing rate as a function of probability $z$')
    figY.show()

    figW = plt.figure(2)
    plt.plot(wdata[:,0], wdata[:,1], 'x')
    plt.xlabel('$z$')
    plt.ylabel('$w$')
    plt.title('Weights as a function of probability $z$')
    figW.show()
    
    figTh = plt.figure(3)
    plt.plot(thdata[:,0], thdata[:,1], 'x')
    plt.xlabel('$z$')
    plt.ylabel(r'$\theta$')
    plt.title('Threshold as a function of probability $z$')
    figTh.show()

    raw_input()

if __name__ == '__main__':
    plot()
