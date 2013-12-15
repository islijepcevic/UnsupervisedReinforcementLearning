from Integrator import *
from Neuron import *
import numpy as np
from Patch import Patch
import random

def loadPatches(filename):
    '''loads patches from one image
    '''

    normalizedFilename = filename.replace('.bmp', '_normalized.data')
    normIn = open(normalizedFilename, 'r')
    normalized = np.fromstring(normIn.read()).reshape(502,758)
    #print np.mean(normalized), np.std(normalized)
    normIn.close()

    patchesFilename = filename.replace('.bmp', '_patches.data')
    patchIn = open(patchesFilename, 'r')
    patchDesc = patchIn.read().split('\n')
    patchIn.close()

    patches = []

    for patchLine in patchDesc:
        if not patchLine:
            continue
        (row, col) = [int(x) for x in patchLine.split()]

        patch = normalized[row:row+16, col:col+16].flatten()
        patches.append(Patch(patch))

    return patches



def load():
    '''loads patches from all images
    '''

    files = []
    for i in xrange(1, 11):
        name = 'images/im' + str(i) + '.bmp'
        files.append(name)

    # list of lot of patches, huge amount of MB
    patches = []

    for filename in files:
        patches += loadPatches(filename)

    return patches


def run():
    patches = load()
    random.shuffle(patches)

    neuron = Neuron()
    integrator = ForwardDifference(neuron)
    #integrator = RungeKutta4(neuron)

    integrator.integrate(patches, 150000)

    #print "\nW_plus"
    #print neuron.wPlus.reshape(16,16)
    #print "W_minus"
    #print neuron.wMinus.reshape(16,16)
    #print "W"
    #print neuron.getW()


import os

if __name__ == "__main__":
    if not os.path.exists('simulation'):
        os.makedirs('simulation')
    run()
