import numpy as np
from plotter import plotOverTime


class Integrator:
    '''class that implements numerical integration in time
    '''
	
    def __init__(self, ode, dt = 1, convergenceThreshold = 1e-3):
        '''ode should be of class ODE
        '''
        self.ode = ode
        self.dt = dt
        self.convergenceThreshold = convergenceThreshold
            
            
    def integrate(self, T = 1000):
        ''' integrate until T
        not needed in exercise 1
        '''
        for t in xrange(T):
            self.nextStep()
            
    def integrateUntilConvergence(self):
        '''integrate until convergence
        modified to do the following:
            -> integrate minimally 2 000 steps
            -> then, if convergence met, stop
            -> integrate maximally 100 000 steps (this raises error)
        new modification:
            -> integrate 50 000 steps, this way much better behavior
            -> convergence reaches every time (2000 was not enough, even though
                the treshold was achieved)
            -> if time graph plotted, oscillations can be observed after the
                convergence - this oscillation is not low and not easily tracked
                with code, so that's why 50 000 was chosen
        '''
        previous = self.ode.getODEState() # numpy array
        i = 0

        toPlot = []
        
        while True:
            toPlot.append( (i, self.ode.w) )

            self.nextStep()
            #if i % 100 == 0:
                #print 'w = %f\ttheta = %f\ty = %f' % (self.ode.w, self.ode.theta,
                #        self.ode.evaluateNeuron(self.ode.x0))
            
            current = self.ode.getODEState()
#            if i > 2000 and np.linalg.norm(previous - current) <= self.convergenceThreshold:
#                break 
            
            previous = current
            i += 1
            self.i = i
            if i > 50000:
                break
                plotOverTime(toPlot)
                raise RuntimeError("did not converge")

        #plotOverTime(toPlot)



            
    def nextStep(self):
        ''' this will perform next step of a particular integration method'''
        raise NotImplementedError
            

class ForwardDifference(Integrator):
    '''basic forward euler integrator'''
    
    def nextStep(self):
        '''do something like:
        s(t+dt) = s(t) + dt * F(s(t)) #where s(k) is the state at step k
        '''
        
        state = self.ode.getODEState()
        nextState = state + self.dt * self.ode.evaluateODERHS(state)
        self.ode.updateODE(nextState)
