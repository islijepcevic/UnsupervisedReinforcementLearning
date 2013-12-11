from pylab import *
from neural_network import NeuralNetwork
import numpy as np
from random import random

# this is a dummy class, use it as template inserting your algorithm.

"""
STATE is encoded with position and velocity vectors (python lists with 2 elems
each)

ENVIRONMENT is encoded with provided class track in track.py

ALGORITHM SKELETON is provided in race.py
"""

class car:
    
    def __init__(self):

        # setup your parameters here.
        
        self.eta = 0.005
        self.gamma = 0.95
        self.Lambda = 0.95
        self.epsilon = 0.1

        self.time = 0
        
        pneurons = 31
        pboundaries = [0.0, 1.0]
        vneurons = 11
        vboundaries = [-1.0, 1.0]
        nbActions = 9
        self.neuralNetwork = NeuralNetwork(pneurons, pboundaries, vneurons, 
                vboundaries, nbActions, self.eta, self.gamma, self.Lambda)

        # store last take action, in order to reinforce eligibility trace
        self.actionIndex = None

    def reset(self) :
    
        # reset values before each trial.
        
        self.time = 0
        self.neuralNetwork.reset()
        self.actionIndex = None

    def choose_action(self, position, velocity, R, learn = True):
        """This method must:
        -choose your action based on the current position and velocity.
        -update your parameters according to SARSA. This step can be turned off
            by the parameter 'learn=False'.

        GIVEN PARAMETERS ARE FOR NEXT STATE, based on PREVIOUS ACTION
        
        The [x,y] values of the position are always between 0 and 1.
        The [vx,vy] values of the velocity are always between -1 and 1.
        The reward from the last action R is a real number
        """

        if self.time == 0:
            # TODO: no learning in first iteration, no previous step (?)
            self.neuralNetwork.computeNetworkOutput(position, velocity)
            self.actionIndex = self.policy()
            return self.neuralNetwork.getActionDirection( self.actionIndex )

        # this copies the list, not a pointer
        Qcurrent = self.neuralNetwork.Qoutputs[:]

        # update neural network to next state
        Qnext = self.neuralNetwork.computeNetworkOutput(position, velocity)
        
        if learn:    
            delta = R + self.gamma*Qnext - Qcurrent

            # updating eligibility trails
            self.neuralNetwork.decayEligibilityTrails(delta)
            self.neuralNetwork.updateEligibilityTrail(self.actionIndex, delta, R)

            # updating weights
            self.neuralNetwork.updateWeights(delta)
            
    	self.time += 1

        # get action, based on policy
        self.actionIndex = self.policy()

    	return self.neuralNetwork.getActionDirection( self.actionIndex )

    def policy(self):
        """this method returns the action index based on some policy
        NOTE: it is assumed that the underlying neural network has already
        computed Q values for given position/velocity
        """
        return self.eGreedyPolicy()


    def eGreedyPolicy(self):
        """this method returns the action index based on epsilon-greedy policy
        NOTE: it is assumed that the underlying neural network has already
        computed Q values for given position/velocity
        """

        Q = self.neuralNetwork.Qoutputs
        assert len(Q) == self.nbActions

        if (np.random.random() < 1-self.epsilon):
            return Q.argmax()
        else:
            # TODO: should we exclude argmax index?
            return Q[random.randint(0, len(Q)-1)]
