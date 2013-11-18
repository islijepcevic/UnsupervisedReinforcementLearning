from ODE import ODE, np
from random import random

class Neuron(ODE):

    def __init__(self, eta = 5e-6, tau = 1200, theta = 5, p = 2):

        self.eta = eta
        self.tau = tau
        self.p = p

        self.wPlus = np.random.normal(0.5, 0.15, 16*16)
        self.wMinus = np.random.normal(0.5, 0.15, 16*16)
        self.theta = theta

        self._checkWeights()


    def getW(self):
        W = self.wPlus - self.wMinus
        return W.reshape(16,16)

    def getODEState(self):
        return np.concatenate((self.wPlus, self.wMinus, np.array([self.theta])))

    def updateODE(self, state):
        self.wPlus = state[:16*16]
        self.wMinus = state[16*16:-1]
        self.theta = state[-1]


    def evaluateODERHS(self, patch, state = None):
        '''
        @param patch - object of class Patch
        @param state - full state array, to enable different integrators
        '''

        y = self.evaluateNeuron(patch, state)
        
        if state is None:
            theta = self.theta
        else:
            theta = state[-1]

        x = np.concatenate((patch.xOn, patch.xOff))

        rhsW = self.eta * x * (y**2 - y*theta) # ndarray
        rhsTheta = 1.0 / self.tau * (y**self.p - theta) # a single float

        return np.concatenate((rhsW, np.array([rhsTheta])))


    def evaluateNeuron(self, patch, state = None):
        '''
        @param patch - object of class Patch
        '''
        if state is None:
            wPlus = self.wPlus
            wMinus = self.wMinus
        else:
            wPlus = state[:16*16]
            wMinus = state[16*16:-1]

        onNetSum = np.dot(wPlus, patch.xOn)
        offNetSum = np.dot(wMinus, patch.xOff)
        netSum = onNetSum + offNetSum

        # transition function
        return max(0.0, netSum)




    def _checkWeights(self):

        self.wPlus = np.maximum(self.wPlus, 0.0)
        self.wMinus = np.maximum(self.wMinus, 0.0)
