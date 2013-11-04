from ODE import ODE, np
from random import random

class BCM(ODE):
	'''This class represents the model of a BCM neuron. At the same time, it 
	is an ordinary differential equation because the neuron changes with time.
	So the object of this class, in ODE sense, represents a state of ODE at 
	some time, and can be evaluated.

	Maybe the better approach would be to make another class for ODE view of 
	a neuron (some kind of adaptor to BCM), but that seemed like an extra effort
	for this task.
	'''
	
	def __init__(self, z, eta = 5e-4, tau = 5e2, x0 = 1, theta0 = 0, w0 = 1, p = 2):
		'''constructor'''
		
		self.z = z
		self.x0 = x0
		
		self.eta = eta
		self.tau = tau
		self.p = p
		
		self.theta = theta0
		self.w = w0
		
		if z < 0 or z > 1:
			raise ValueError("z should be in [0,1]")
		
		
	def getODEState(self):
		'''returns the state of the ODE: numpy array of the weight w and
		parameter theta'''
		return np.array([self.w, self.theta])
		
	def updateODE(self, state):
		'''updates the parameters that change withtime'''
		self.w = state[0]
		self.theta = state[1]
		
		
	def evaluateODERHS(self, state = None):
		'''evaluates the ODE right hand side (the learning rule)'''
		if state is None:
			state = self.getODEState()
			
		w = state[0]
		theta = state[1]
			
		x = self.generateNeuronInput()
		y = self.evaluateNeuron(x, w)
		
		rhs_w = self.eta * x * (y**2 - y*theta)
		rhs_theta = 1.0/self.tau * (y**self.p - theta)
		
		return np.array([rhs_w, rhs_theta])


	def evaluateNeuron(self, x = None, w = None):
		'''evaluates the neuron
		@param x - force some value of x, if provided
		@param w - use another weight w, if provided
		'''
		if x is None:
			x = self.generateNeuronInput()
		
		if w is None:
			w = self.w
			
		netsum = w*x
		
		return self.transitionFunction(netsum)

	def generateNeuronInput(self):
		'''computes input of the neuron, which is x0 with probability z,
		and 0 with probability (1-z)
		'''
		val = random()
		if val <= self.z:
			return self.x0
		return 0.0
				
				
	def transitionFunction(self, netsum):
		'''transition f(.) of the output neuron'''
		return max(0, netsum)
