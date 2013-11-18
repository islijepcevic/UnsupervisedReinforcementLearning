import numpy as np

class Patch:

    def __init__(self, patch):
        '''
        @param patch - numpy array, 1D, size 16x16
        '''

        self.xOn = np.maximum(patch, 0.0)
        self.xOff = np.minimum(patch, 0.0)
