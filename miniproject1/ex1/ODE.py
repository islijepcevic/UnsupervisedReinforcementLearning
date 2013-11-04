import numpy as np

class ODE:
	''' abstract model of diferential equation'''
	
	def getODEState(self):
		'''Needs to return a ndarray'''
		raise NotImplementedError

	def updateODE(self, state):
		'''state must be ndarray'''
		raise NotImplementedError
		
	def evaluateODERHS(self):
		raise NotImplementedError
