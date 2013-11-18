from BCM import BCM
from Integrator import ForwardDifference

import sys

def simulate():
    for zz in xrange(20, 81, 2):
        z = zz / 100.0

        print >> sys.stderr, 'simulating for %f' % z
        
        # create new neuron with input probability z
        bcm = BCM(z)
        # create new integrator
        integrator = ForwardDifference(bcm)
        
        try:
            # do the integration
            integrator.integrateUntilConvergence()

        except RuntimeError as re:
            # prints "did not converge"
            print re.args[0]
           
        print z, bcm.evaluateNeuron(bcm.x0), bcm.w, bcm.theta, integrator.i

if __name__ == '__main__':
    simulate()
