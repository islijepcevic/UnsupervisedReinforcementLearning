import numpy as np
from plotter import *

class Integrator:
	
    def __init__(self, ode, dt = 1, convergenceThreshold = 1e-5):
        '''ode should be of class ODE
        '''
        self.ode = ode
        self.dt = dt
        self.convergenceThreshold = convergenceThreshold
            
            
    def integrate(self, neuronInput, T = 1000):
        '''integrates the total of T timesteps
        at each iteration presents a patch from list neuronInput
        list iteration is circular
        @param neuronInput - list of patches for input
        '''

        fl = open('theta.data', 'w')

        N = len(neuronInput)

        plot(self.ode, 0)

        for t in xrange(T):
            self.nextStep(neuronInput[t%N])

            if (t+1)%10000 == 0:
                plot(self.ode, t+1)
            
            th = str(t) + ' ' + str(self.ode.theta) + '\n'
            fl.write(th)

        fl.close()
        plotTheta()

            
    def nextStep(self, inputPatch):
        ''' this will perform next step of a particular integration method'''
        raise NotImplementedError
            

class ForwardDifference(Integrator):
    '''basic forward Euler integrator'''
    
    def nextStep(self, inputPatch):
        # do something like:
        # s(t+dt) = s(t) + dt * F(s(t)) #where s(k) is the state at step k
        
        state = self.ode.getODEState()
        nextState = state + self.dt * self.ode.evaluateODERHS(inputPatch, state)
        self.ode.updateODE(nextState)

class RungeKutta4(Integrator):
    '''runge kutta 4 integrator'''

    def nextStep(self, inputPatch):

        state = self.ode.getODEState()

        k1 = self.ode.evaluateODERHS(inputPatch, state)
        k2 = self.ode.evaluateODERHS(inputPatch, state + self.dt * 0.5 * k1)
        k3 = self.ode.evaluateODERHS(inputPatch, state + self.dt * 0.5 * k2)
        k4 = self.ode.evaluateODERHS(inputPatch, state + self.dt * k3)

        nextState = state + self.dt / 6.0 * (k1 + 2.0*k2 + 2.0*k3 + k4)

        self.ode.updateODE(nextState)
