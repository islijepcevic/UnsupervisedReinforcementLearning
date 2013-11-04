import numpy as np

class Integrator:
	
	def __init__(self, ode, dt = 1, convergenceThreshold = 1e-5):
		'''ode should be of class ODE
		'''
		self.ode = ode
		self.dt = dt
		self.convergenceThreshold = convergenceThreshold
		
		
	def integrate(self, T = 1000):
		# integrate until T
		# probably not needed
		for t in xrange(T):
			self.nextStep()
		pass
		
	def integrateUntilConvergence(self):
		previous = self.ode.getODEState() # numpy array
		i = 0
		
		while True:
			self.nextStep()
			
			current = self.ode.getODEState()
			if np.linalg.norm(previous - current) <= self.convergenceThreshold:
				break 
			
			previous = current
			i += 1
			if i > 100000:
				raise RuntimeError("did not converge")
		
	def nextStep(self):
		''' this will perform next step of a particular integration method'''
		raise NotImplementedError
		

class ForwardDifference(Integrator):
	
	def nextStep(self):
		# do something like:
		# s(t+dt) = s(t) + dt * F(s(t)) #where s(k) is the state at step k
		
		state = self.ode.getODEState()
		nextState = state + self.dt * self.ode.evaluateODERHS(state)
		self.ode.updateODE(nextState)
