import matplotlib.pyplot as plt
import numpy as np

import sys

def getPointsForFitting(data):
    zInterval = []
    w = []
    lastZ = None
    count = 0
    nbZs = -1
    for z, w_now in zip(data[:,0], data[:,1]):
        if z != lastZ:
            lastZ = z
            count = 0
            nbZs += 1
            zInterval.append(z)
            w.append(0.0)

        w[nbZs] = float(count)/(count+1)*w[nbZs] + w_now/(count+1.0)
        count += 1

    interval = np.array(zInterval)
    values = np.array(w)

    assert (len(interval) == len(values))

    return interval, values

def fit_exponential(t, y, C=0):
    y = y - C
    y = np.log(y)
    K, A_log = np.polyfit(t, y, 1)
    A = np.exp(A_log)
    return A, K

def exponential(data):

    (zInterval, w) = getPointsForFitting(data)

    #C = np.mean(data[-5:, 1] - 0.05)
    C = w[-1]
    A, K = fit_exponential(zInterval[1:-1], w[1:-1], C)
    myexp = A * np.exp(K * zInterval) + C

    return (zInterval, myexp)

def fit_polynomial(data, deg = 2):

    (zInterval, w) = getPointsForFitting(data)
    coeffs = np.polyfit(zInterval, w, deg)

    poly = np.poly1d(coeffs)
    curve = poly(zInterval)

    return zInterval, curve


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

    # exponential          
    (expInterval, curveExp) = exponential(data)
    (polyInterval, curvePoly) = fit_polynomial(data, 4)

    # plot
    figY = plt.figure(1)
    plt.plot(data[:,0], data[:,1], 'x', label="Simulated weights")
    plt.plot(expInterval, curveExp, 'r-', label="exponential fit")
    plt.plot(polyInterval, curvePoly, 'g-', label="polynomial order 4 fit")
    plt.xlabel('$z$')
    plt.ylabel('$y$')
    plt.title('Firing rate as a function of probability $z$')
    plt.legend(loc='upper right', shadow=True)
    figY.show()

    #figW = plt.figure(2)
    #plt.plot(wdata[:,0], wdata[:,1], 'x')
    #plt.xlabel('$z$')
    #plt.ylabel('$w$')
    #plt.title('Weights as a function of probability $z$')
    #figW.show()
    #
    #figTh = plt.figure(3)
    #plt.plot(thdata[:,0], thdata[:,1], 'x')
    #plt.xlabel('$z$')
    #plt.ylabel(r'$\theta$')
    #plt.title('Threshold as a function of probability $z$')
    #figTh.show()

    raw_input()

def plotOverTime(data):
    data = np.array(data)

    plt.plot(data[:,0], data[:,1])
    plt.show()

if __name__ == '__main__':
    plot()
