from pylab import *

# this is a dummy class, use it as template inserting your algorithm.

class car:
    
    def __init__(self):

        # setup your parameters here.
        
        self.n_actions = 9
        #self.n_neurons = ...
        #self.weights = zeros(...)

    def reset(self) :
    
        # reset values before each trial.
        
        self.time = 0
        #self.eligibility_trace = zeros(...)

    def choose_action(self, position, velocity, R, learn = True):
        # This method must:
        # -choose your action based on the current position and velocity.
        # -update your parameters according to SARSA. This step can be turned off by the parameter 'learn=False'.
        #
        # The [x,y] values of the position are always between 0 and 1.
        # The [vx,vy] values of the velocity are always between -1 and 1.
        # The reward from the last action R is a real number

    	action = int(rand()*9)				                       # dummy random choice
    	
    	# add your action choice algorithm here
        
        if learn:    
            # add your learning algorithm here
    	
            #self.weights += ...
            
    	self.time += 1

    	return action











       