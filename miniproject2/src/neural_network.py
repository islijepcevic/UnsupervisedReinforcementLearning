import numpy as np
import plotter
import params

class NeuralNetwork:
    """this  class models the specific neural network for the car race
number of input neurons is variable, both for positions and velocities
number of output neurons also
"""

    def __init__(self, pos_neurons, pos_boundaries, vel_neurons, vel_boundaries, nb_outputs,
            eta, gamma, Lambda):
        """constructor
        @param pos_neurons number of neurons per axis for encoding position
        @param pos_boundaries the interval
        @param vel_neurons number of neurons per axis for encoding velocity
        @param vel_boundaries the interval
        @param nb_outputs number of output neurons (should be 9 to be compatible
            with track.py)
        @param eta, gamma, lambda - learning algorithm parameters
        """

        # these are "centers" of neuron encodings

        positions = np.linspace(pos_boundaries[0], pos_boundaries[1], pos_neurons)       
        velocities = np.linspace(vel_boundaries[0], vel_boundaries[1], vel_neurons)
       
        
        (px, py) = np.meshgrid(positions, positions)
                #, sparse = False, indexing = 'xy')
        self.pos_deviation_2 = np.square(px[0][1]-px[0][0])
        (vx, vy) = np.meshgrid(velocities, velocities)
            #, sparse = False, indexing = 'xy')
        self.vel_deviation_2 = np.square(vx[0][1] - vx[0][0])

        # neuron centers
        self.positions_x = px.flatten()
        self.positions_y = py.flatten()
        self.velocities_x = vx.flatten()
        self.velocities_y = vy.flatten()

        self.nb_pos_cells = pos_neurons*pos_neurons
        self.nb_vel_cells = vel_neurons*vel_neurons
        self.nb_all_cells = self.nb_pos_cells + self.nb_vel_cells

        self.inputs = np.zeros(self.nb_all_cells)

        self.nb_outputs = nb_outputs

        # for each output neuron, we have weights and traces
        self.weights = np.zeros((nb_outputs,self.nb_all_cells))
        self.el_traces = np.zeros((nb_outputs,self.nb_all_cells))
        self.Q_outputs = np.zeros(self.nb_outputs)
        
        self.time = 0
        self.iter = 0

        self.eta = eta
        self.gamma = gamma
        self.Lambda = Lambda
        
    def reset(self):
        '''
        self.time = 0
        self.iter += 1'''
        self.el_traces = np.zeros((params.NB_OUTPUTS,self.nb_all_cells))

    def _set_network_input(self, pos, vel):
        # given current position and velocity, set the position and velocity inputs
        term1 = np.square(pos[0] - self.positions_x)
        term2 = np.square(pos[1] - self.positions_y)
        exponent = -(term1 + term2) / 2.0 / self.pos_deviation_2
        # flatten as you pack pre-synaptic firing rates into the input array
        self.inputs[:self.nb_pos_cells] = np.exp(exponent)
        
        
        term1 = np.square(vel[0] - self.velocities_x) 
        term2 = np.square(vel[1] - self.velocities_y)
        exponent = -(term1 + term2) / 2.0 / self.vel_deviation_2
        # flatten as you pack pre-synaptic firing rates into the input array
        self.inputs[self.nb_pos_cells:] = np.exp(exponent)
        
        
    def compute_network_output(self, pos, vel):
        # calculate and set the inputs given position and velocity
        self._set_network_input(pos, vel)
        # calculate the output of each neuron: this is the Q value
        self.Q_outputs= np.dot(self.weights, self.inputs)
        # Deniz: removed return statement for class attribute self.Q_outputs. 
       

    def decay_eligibility_trails(self):
        """decays all eligibility trails"""
        
        self.el_traces *= (self.gamma * self.Lambda)
         

    def update_eligibility_trail(self, takenAction):
        """updates the last taken eligibility trail"""
        self.el_traces[takenAction] += self.inputs # TODO: which r_j? weighted??

    def update_weights(self, delta, action):
        """updates all weights"""
        # print "delta:", delta
        
    #    self.time += 1
        self.weights[action] += (self.eta * delta * self.el_traces[action])
        '''
        plotter.plotWeights(self.weights[action])
        
        print "plotting weights"
        plotter.plotWeights(self.weights[action])
        for k in xrange(len(self.weights)):
            print k
            print self.weights[k]
        raw_input()
        '''    
if __name__ == "__main__":
    new_network = NeuralNetwork(params.POS_NEURONS, params.POS_RANGE, params.VEL_NEURONS, 
                params.VEL_RANGE, params.NB_OUTPUTS, params.ETA, params.GAMMA, params.LAMBDA)  
    pos = np.array([0.05,0.03])
    vel =  np.array([0,0])
    new_network._set_network_input(pos,vel)
    
        # array += scalar*scalar*array, arrays are 2D
    #self.weights += self.eta * delta * self.el_traces

