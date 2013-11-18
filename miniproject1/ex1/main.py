from BCM import BCM
from Integrator import ForwardDifference

import sys

def simulate():
    for zz in xrange(20, 81, 2):
        z = zz / 100.0

        print >> sys.stderr, 'simulating for %f' % z
        
        bcm = BCM(z)
        integrator = ForwardDifference(bcm)
        
        try:
            integrator.integrateUntilConvergence()
            #print z, bcm.evaluateNeuron(bcm.x0)

        except RuntimeError as re:
            print re.args[0]
           
        print z, bcm.evaluateNeuron(bcm.x0), integrator.i

if __name__ == '__main__':
    simulate()
