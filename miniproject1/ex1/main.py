from BCM import BCM
from Integrator import ForwardDifference

if __name__ == '__main__':
	
	for zz in xrange(2, 9, 1):
		z = zz / 10.0
		
		bcm = BCM(z)
		integrator = ForwardDifference(bcm)
		
		integrator.integrateUntilConvergence()
		
		print z, bcm.evaluateNeuron(bcm.x0)
		
