import numpy as np

class Integrator:
	
    def __init__(self, ode, dt = 1, convergenceThreshold = 1e-5):
        '''ode should be of class ODE
        '''
        self.ode = ode
        self.dt = dt
        self.convergenceThreshold = convergenceThreshold
            
            
    def integrate(self, neuronInput, T = 1000):
        # integrate until T

        N = len(neuronInput)

        for t in xrange(T):
            self.nextStep(neuronInput[t%N])
            
    def nextStep(self, inputPatch):
        ''' this will perform next step of a particular integration method'''
        raise NotImplementedError
            

class ForwardDifference(Integrator):
    
    def nextStep(self, inputPatch):
        # do something like:
        # s(t+dt) = s(t) + dt * F(s(t)) #where s(k) is the state at step k
        
        state = self.ode.getODEState()
        nextState = state + self.dt * self.ode.evaluateODERHS(inputPatch, state)
        self.ode.updateODE(nextState)

class RunkeKutta4(Integrator):

    def nextStep(self, inputPatch):

        state = self.ode.getODEState()

        k1 = self.ode.evaluateODERHS(inputPatch, state)
        k2 = self.ode.evaluateODERHS(inputPatch, state + self.dt * 0.5 * k1)
        k3 = self.ode.evaluateODERHS(inputPatch, state + self.dt * 0.5 * k2)
        k4 = self.ode.evaluateODERHS(inputPatch, state + self.dt * k3)

        nextState = state + self.dt / 6.0 * (k1 + 2.0*k2 + 2,0*k3 + k4)

        self.ode.updateODE(nextState)
