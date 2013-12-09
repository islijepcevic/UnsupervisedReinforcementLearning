import numpy as np

""" THIS FILE IS ACTUALLY NOT NEEDED
FOR STATE, JUST USE VECTORS:
    position
    velocity

FOR ENVIRONMENT, USE:
    track
"""
class State:

    def __init__(self, p, v):
        """constructor
        @param p - 2D vector p (numpy array or python list)
        @param v - 2D vector v (numpy array or python list)
        """
        assert len(p) == 2 and len(v) == 2
        self._s = np.zeros(4)
        self._s[:2] = p
        self._s[2:] = v

    def getPosition(self):
        """returns numpy array!!!"""
        return self._s[:2]

    def getVelocity(self):
        """returns numpy array!!!"""
        return self._s[2:]

    def setPosition(self, pos):
        """setter for position
        @param pos - could be numpy array or python list
        """
        self._s[:2] = pos

    def setVelocity(self, vel):
        """setter for velocity
        @param vel - could be numpy array or python list
        """
        self._s[2:] = vel


class Environment:

    def __init__(self, theTrack):
        '''constructor
        @param theTrack - instance of track object, already setup
        '''
        self.track = Track
