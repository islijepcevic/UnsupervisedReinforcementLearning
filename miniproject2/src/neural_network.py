import numpy as np


class NeuralNetwork:
"""this  class models the specific neural network for the car race
number of input neurons is variable, both for positions and velocities
number of output neurons also
"""

    def __init__(self, pneurons, pboundaries, vneurons, vboundaries, noutputs):
        """constructor
        @param pneurons number of neurons per axis for encoding position
        @param pboundaries the interval
        @param vneurons number of neurons per axis for encoding velocity
        @param vboundaries the interval
        @param noutputs number of output neurons (should be 9 to be compatible
            with track.py)
        """

        # these are "centers" of neuron encodings
        self.positions = np.linspace(pboundaries[0], pboundaries[1], pneurons)
        self.velocities = np.linspace(vboundaries[0], vboundaries[1], vneurons)

        self.posDeviation = self.positions[1] - self.positions[0]
        self.velDeviation = self.velocities[1] - self.velocities[0]

        self.npos = pneurons*pneurons
        self.nvel = vneurons*vneurons
        self.ntotal = self.npos + self.nvel

        self.inputs = np.zeros(self.ntotal)

        self.noutputs = noutputs

        # list (for each action) of np arrays
        self.weights = []
        self.etraces = []
        self.Qoutputs = []
        for i in xrange(noutputs):
            self.weigts.append( np.zeros(self.ntotal) )
            self.etraces.append( np.zeros(self.ntotal) )
            self.Qoutputs.append(0.0)

    def reset(self):
        for i in xrange(len(self.etraces)):
            self.etraces[i] = np.zeros(self.ntotal)

    def _setNetworkInput(self, pos, vel):
        """given current position and velocity, set the network's input values"""
        for i in xrange(len(self.positions)):
            for j in xrange(len(self.positions)):

                term1 = np.square(pos[0] - self.positions[i]) 
                term2 = np.square(pos[1] - self.positions[j])
                exponent = -(term1 + term2) / 2.0 / np.square(self.posDeviation)

                index = i*len(self.positions) + j
                self.inputs[index] = np.exp(exponent)

        for i in xrange(len(self.velocities)):
            for j in xrange(len(self.velocities)):

                term1 = np.square(vel[0] - self.velocities[i]) 
                term2 = np.square(vel[1] - self.velocities[j])
                exponent = -(term1 + term2) / 2.0 / np.square(self.velDeviation)

                index = self.npos + i*len(self.velocities) + j
                self.inputs[index] = np.exp(exponent)


    def computeNetworkOutput(self, pos, vel):
        """computes Q values
        returns Q values (but also stores them)
        """
        self._setNetworkInput(pos, vel)
        for i in xrange(len(self.Qoutputs)):
            self.Qoutputs[i] = np.dot(self.weights[i], self.inputs)

        return self.Qoutputs

    def getActionDirection(self, a):
        """computes the direction for action a
        @param a - integer, index to Q value list
        """

        if a == 0:
            return [0.0, 0.0]

        ndir = self.noutputs - 1

        dirx = np.cos(-2.0*np.pi*a/ndir + np.pi/2.0)
        diry = np.sin(-2.0*np.pi*a/ndir + np.pi/2.0)

        return (dirx, diry)
