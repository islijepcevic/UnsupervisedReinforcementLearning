from neural_network import NeuralNetwork
import numpy as np
import params
# this is a dummy class, use it as template inserting your algorithm.

"""
STATE is encoded with position and velocity vectors (python lists with 2 elems
each)

ENVIRONMENT is encoded with provided class track in track.py

ALGORITHM SKELETON is provided in race.py
"""

class car:
    
    def __init__(self):

        # Deniz: moved parameters to params.py
        
        self.time = 0
        self.neuralNetwork = NeuralNetwork(params.POS_NEURONS, params.POS_RANGE, 
                params.VEL_NEURONS, params.VEL_RANGE, params.NB_OUTPUTS, 
                params.ETA, params.GAMMA, params.LAMBDA)

        # store last take action, in order to reinforce eligibility trace
        self.action_index = None

    def reset(self) :
    
        # reset values before each trial.
        
        self.time = 0
        self.neuralNetwork.reset()
        self.action_index = None

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
            self.neuralNetwork.compute_network_output(position, velocity)
            self.action_index = self.policy()
            self.time += 1
            return self.action_index
            #return self.neuralNetwork.getActionDirection( self.action_index )

        if learn:
            # updating eligibility trails
            # do it before everything else, since eligibility traces are
            # reinforced with the input of the taken action (== previous action)
            # so before we change input to new position
            #print "I'm learning"
            self.neuralNetwork.decay_eligibility_trails()
            self.neuralNetwork.update_eligibility_trail(self.action_index)
#            pass

        # this copies the list by slicing, not a pointer
        Q_current = self.neuralNetwork.Q_outputs[self.action_index]

        # get new Q values after the transition Q(s',a')
        self.neuralNetwork.compute_network_output(position, velocity)
        # get action a', based on policy
        new_action = self.policy()
        Q_next = self.neuralNetwork.Q_outputs[new_action]

        if learn:    
#            if R>0:
#                R *= (1000 / self.time)
#            else:
#                R /= 2.0
            delta = R + params.GAMMA*Q_next - Q_current

# ivan: wrong place for updating etraces
#            self.neuralNetwork.decay_eligibility_trails()
#            self.neuralNetwork.update_eligibility_trail(self.action_index)

            # updating weights
            self.neuralNetwork.update_weights(delta, self.action_index)

# ivan: same as putting it up before everything
#            self.neuralNetwork.decay_eligibility_trails()
#            self.neuralNetwork.update_eligibility_trail(new_action)


        self.time += 1

        
        self.action_index = new_action

        # actuate the action a'
        return self.action_index

    def get_action_direction(self, a):
        """computes the direction for action a
        @param a - integer, index to Q value list
        """
        # return constant velocity (0,0) if a = 0 
        if a == 0:
            return (0.0, 0.0)

        n_dir = params.NB_OUTPUTS - 1.0

        dir_x = np.cos(-2.0*np.pi*a/n_dir + np.pi/2.0)
        dir_y = np.sin(-2.0*np.pi*a/n_dir + np.pi/2.0)

        return (dir_x, dir_y)

    def policy(self):
        """this method returns the action index based on some policy
        NOTE: it is assumed that the underlying neural network has already
        computed Q values for given position/velocity
        """
        #return self.decaying_e_greedy_policy()
        return self.e_greedy_policy()

    def decaying_e_greedy_policy(self):
        """this method returns the action index based on epsilon-greedy policy
        NOTE: it is assumed that the underlying neural network has already
        computed Q values for given position/velocity
        """

        Q = self.neuralNetwork.Q_outputs
        assert len(Q) == params.NB_OUTPUTS

        if self.time < params.STOP_DECAY:
            delta_eps = params.EPSILON_START - params.EPSILON
            eps = -delta_eps*self.time/params.STOP_DECAY + params.EPSILON_START
        else: 
            eps = params.EPSILON

        threshold = (1 - eps)

        if np.random.random() < threshold:
            return Q.argmax() #this returns index
        else:
            return np.random.randint(0, len(Q)-1) #this returns value!


    def e_greedy_policy(self):
        """this method returns the action index based on epsilon-greedy policy
        NOTE: it is assumed that the underlying neural network has already
        computed Q values for given position/velocity
        """

        Q = self.neuralNetwork.Q_outputs
        assert len(Q) == params.NB_OUTPUTS

        if (np.random.random() < 1-params.EPSILON):
            argmx = Q.argmax()
            if abs(Q[argmx] - 0.0) <= 1e-6:
                return np.random.randint(0, len(Q)-1) #this returns value!
            return Q.argmax() #this returns index
        else:
            return np.random.randint(0, len(Q)) #this returns value!
