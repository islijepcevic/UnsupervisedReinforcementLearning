from Integrator import *
from Neuron import *
import numpy as np
from Patch import Patch

def loadPatches(filename):
    '''loads patches from one image
    '''

    normalizedFilename = filename.replace('.bmp', '_normalized.data')
    normIn = open(normalizedFilename, 'r')
    normalized = np.fromstring(normIn.read()).reshape(502,758)
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

    neuron = Neuron()
    integrator = ForwardDifference(neuron)
    #integrator = RunkeKutta4(neuron)

    integrator.integrate(patches, 150000)


if __name__ == "__main__":
    run()
