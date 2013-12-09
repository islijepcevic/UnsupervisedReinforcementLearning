import numpy as np


class NeuralNetwork:
"""this  class models the specific neural network for the car race
number of input neurons is variable, both for positions and velocities
number of output neurons also
"""

    def __init__(self, pneurons, pboundaries, vneurons, vboundaries, noutputs):
        """constructor
        @param pneurons tuple (pair) of neurons per X and Y axis for
            encoding position
        @param pboundaries list of lists: for every neuron, the interval
        @param vneurons tuple (pair) of neurons per X and Y axis for
            encoding velocity
        @param vboundaries list of lists: for every neuron, the interval
        @param noutputs number of output neurons
        """

        # these are "centers" of neuron encodings
        self.xPositions = np.linspace(pboundaries[0][0], pboundaries[0][1], pneurons[0])
        self.yPositions = np.linspace(pboundaries[1][0], pboundaries[1][1], pneurons[1])
        self.xVelocities = np.linspace(vboundaries[0][0], vboundaries[0][1], vneurons[0])
        self.yVelocities = np.linspace(vboundaries[1][0], vboundaries[1][1], vneurons[1])

        self.npos = pneurons[0]*pneurons[1]
        self.nvel = vneurons[0]*vneurons[1]
        self.ntotal = self.npos + self.nvel

        self.noutputs = noutputs

        # list (for each action) of np arrays
        self.weights = []
        self.etraces = []
        for i in xrange(noutputs):
            self.weigts.append( np.zeros(self.ntotal) )
            self.etraces.append( np.zeros(self.ntotal) )

    def reset(self):
        for i in xrange(len(self.etraces)):
            self.etraces[i] = np.zeros(self.ntotal)

    def set_network_input(self):
        pass

    def compute_network_output(self, x, y):
        """computes Q values"""
        pass
