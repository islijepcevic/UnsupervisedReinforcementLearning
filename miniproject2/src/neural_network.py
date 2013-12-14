import numpy as np


class NeuralNetwork:
    """this  class models the specific neural network for the car race
number of input neurons is variable, both for positions and velocities
number of output neurons also
"""

    def __init__(self, pneurons, pboundaries, vneurons, vboundaries, noutputs,
            eta, gamma, Lambda):
        """constructor
        @param pneurons number of neurons per axis for encoding position
        @param pboundaries the interval
        @param vneurons number of neurons per axis for encoding velocity
        @param vboundaries the interval
        @param noutputs number of output neurons (should be 9 to be compatible
            with track.py)
        @param eta, gamma, lambda - learning algorithm parameters
        """

        # these are "centers" of neuron encodings
        positions = np.linspace(pboundaries[0], pboundaries[1], pneurons)
        velocities = np.linspace(vboundaries[0], vboundaries[1], vneurons)

        (px, py) = np.meshgrid(positions, positions, sparse = False, 
                                        indexing = 'xy')

        (vx, vy) = np.meshgrid(velocities, velocities, sparse = False,
                                        indexing = 'xy')

        # neuron centers
        self.px = px.flatten()
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

        self.eta = eta
        self.gamma = gamma
        self.Lambda = Lambda

    def reset(self):
        for i in xrange(len(self.etraces)):
            self.etraces[i] = np.zeros(self.ntotal)

    def _setNetworkInput(self, pos, vel):
        """given current position and velocity, set the network's input values"""

        # position inputs
        term1 = np.square(pos[0] - self.px) 
        term2 = np.square(pos[1] - self.py)
        exponent = -(term1 + term2) / 2.0 / np.square(self.posDeviation)

        self.inputs[:self.npos] = np.exp(exponent)

        # velocity inputs
        term1 = np.square(vel[0] - self.vx) 
        term2 = np.square(vel[1] - self.vy)
        exponent = -(term1 + term2) / 2.0 / np.square(self.velDeviation)

        self.inputs[self.npos:] = np.exp(exponent)


    def computeNetworkOutput(self, pos, vel):
        """computes Q values
        returns Q values (but also stores them)
        """
        self._setNetworkInput(pos, vel)

        # matrix-vector product
        self.Qoutputs = self.weights.dot( self.inputs )

        return self.Qoutputs

    def getActionDirection(self, a):
        """computes the direction for action a
        @param a - integer, index to Q value list
        """

        if a == 0:
            return (0.0, 0.0)

        ndir = self.noutputs - 1

        dirx = np.cos(-2.0*np.pi*a/ndir + np.pi/2.0)
        diry = np.sin(-2.0*np.pi*a/ndir + np.pi/2.0)

        return (dirx, diry)

    def decayEligibilityTrails(self, delta):
        """decays all elibility trails"""
        # TODO: formula states that only the traces in state 'j' decay;
        #   but what is 'j'? Here, states are continuous. It seems natural
        #   to decay everything.
        #   Formulas taken from slide 39, week 18-24 November slides
        for i in xrange(self.noutputs):
            self.etrace[i] = self.gamma * self.Lambda * self.etrace[i]

    def updateEligibilityTrail(self, takenAction, delta, reward):
        """updates the last taken eligibility trail"""
        self.etrace[takenAction] += reward # TODO: NOT REWARD, PRESYNAPTIC FIRING RATE

    def updateWeights(self, delta):
        """updates all weights"""
        # array += scalar*scalar*array, arrays are 2D
        self.weights += self.eta * delta * self.etrace
