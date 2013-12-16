import numpy as np
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
       
        
        (px, py) = np.meshgrid(positions, positions, sparse = False, 
                                        indexing = 'xy')
        self.pos_deviation = px[0][1]-px[0][0]
        (vx, vy) = np.meshgrid(velocities, velocities, sparse = False,
                                        indexing = 'xy')
        self.vel_deviation = vx[0][1] - vx[0][0]
        # Deniz: No flattening just yet -- otherwise we can't compute the activity of the place cells
        # neuron centers
        self.positions_x = px.flatten() # FLATTEN POSITIONS AND VELS LIKE THIS
        self.positions_y = py.flatten()
        self.velocities_x = vx.flatten()
        self.velocities_y = vy.flatten()
        '''
        print "pos x:", self.positions_x
        print "pos y:", self.positions_y
        print "vel x:", self.velocities_x
        print "vel y:", self.velocities_y
        '''      
        self.nb_pos_cells = pos_neurons*pos_neurons
        self.nb_vel_cells = vel_neurons*vel_neurons
        self.nb_all_cells = self.nb_pos_cells + self.nb_vel_cells

        self.inputs = np.zeros(self.nb_all_cells)

        self.nb_outputs = nb_outputs

        # for each output neuron, we have weights and traces
        self.weights = np.zeros((nb_outputs,self.nb_all_cells))
        self.el_traces = np.zeros((nb_outputs,self.nb_all_cells))
        self.Q_outputs = np.zeros(self.nb_outputs)
        
        # Deniz:  not sure why you added the stuff below again -- it's the same as what's above this comment...? 
        
        '''
        positions = np.linspace(pboundaries[0], pboundaries[1], pneurons)
        velocities = np.linspace(vboundaries[0], vboundaries[1], vneurons)

        (px, py) = np.meshgrid(positions, positions, sparse = False, 
                                        indexing = 'xy')

        (vx, vy) = np.meshgrid(velocities, velocities, sparse = False,
                                        indexing = 'xy')

        # Deniz: No flattening just yet -- otherwise we can't compute the activity of the place cells
        # neuron centers
        self.px = px.flatten() # FLATTEN POSITIONS AND VELS LIKE THIS
        self.py = py.flatten()
        self.vx = vx.flatten()
        self.vy = vy.flatten()

        # neuron center distances == standard deviations for computing input values
        self.posDeviation = positions[1] - positions[0]
        self.velDeviation = self.velocities[1] - self.velocities[0]

        self.npos = pneurons*pneurons
        self.nvel = vneurons*vneurons
        self.ntotal = self.npos + self.nvel

        self.inputs = np.zeros(self.ntotal)

        self.noutputs = noutputs

        # 2D arrays (same as matrices, but let's not complicate)
        self.weights = np.zeros((noutputs, self.ntotal))
        self.etraces = np.zeros((noutputs, self.ntotal))
        self.Qoutputs = np.zeros(self.noutputs) # this one is 1D
        '''

        self.eta = eta
        self.gamma = gamma
        self.Lambda = Lambda
        
    def reset(self):

        self.el_traces = np.zeros((params.NB_OUTPUTS,self.nb_all_cells))

    def _set_network_input(self, pos, vel):
        # given current position and velocity, set the position and velocity inputs
        term1 = np.square(pos[0] - self.positions_x)
        #    print  "term1:", term1
        term2 = np.square(pos[1] - self.positions_y)
        #print "term2:", term2
        exponent = -(term1 + term2) / 2.0 / np.square(self.pos_deviation)
        #     print "exp:",exponent
        # flatten as you pack pre-synaptic firing rates into the input array
        self.inputs[:self.nb_pos_cells] = np.exp(exponent)
        
        
        term1 = np.square(vel[0] - self.velocities_x) 
        term2 = np.square(vel[1] - self.velocities_y)
        exponent = -(term1 + term2) / 2.0 / np.square(self.vel_deviation)
        # flatten as you pack pre-synaptic firing rates into the input array
        self.inputs[self.nb_pos_cells:] = np.exp(exponent)
        
        
    def compute_network_output(self, pos, vel):
        # calculate and set the inputs given position and velocity
        self._set_network_input(pos, vel)
        # calculate the output of each neuron: this is the Q value
        self.Q_outputs= np.dot(self.weights, self.inputs)
        # Deniz: removed return statement for class attribute self.Q_outputs. 
       
        ''' 
    # put this in car.py
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
        '''
    def decay_eligibility_trails(self):
        """decays all eligibility trails"""
        # TODO: formula states that only the traces in state 'j' decay;
        #   but what is 'j'? Here, states are continuous. It seems natural
        #   to decay everything.
        #   Formulas taken from slide 39, week 18-24 November slides
        
        self.el_traces *= (self.gamma * self.Lambda)
         

    def update_eligibility_trail(self, takenAction):
        """updates the last taken eligibility trail"""
        self.el_traces[takenAction] += self.inputs # TODO: which r_j? weighted??

    def update_weights(self, delta):
        """updates all weights"""
        # print "delta:", delta
        self.weights += self.eta * np.dot(delta,self.el_traces) # TODO check this works
            
if __name__ == "__main__":
    new_network = NeuralNetwork(params.POS_NEURONS, params.POS_RANGE, params.VEL_NEURONS, 
                params.VEL_RANGE, params.NB_OUTPUTS, params.ETA, params.GAMMA, params.LAMBDA)  
    pos = np.array([0.05,0.03])
    vel =  np.array([0,0])
    new_network._set_network_input(pos,vel)
    
        # array += scalar*scalar*array, arrays are 2D
    #self.weights += self.eta * delta * self.el_traces

