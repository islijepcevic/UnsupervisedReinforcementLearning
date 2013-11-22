import math 
import random 
import numpy as np
import copy
import pylab
random.seed(0)

NUM_NEURONS = 100
TIME_LIMIT = 50000
MU_RANGE = 5
NUM_EXPTS = 30
eta = 5.0*(10**(-2))
tau = 1.0*(10**(2))
dt = 1.0
x_0 =  1.0
sig_y = 0.0
sig2_y = 0.0
F = 0.0
sigma = 10.0
constant = 1.0/math.sqrt(2*math.pi*(sigma**2))



for experiment in range(NUM_EXPTS): #simulate the paradigm using many different initializations of w_0
	mu = [(20.0*j)+10.0 for j in range(MU_RANGE)]
	y = []	
	y2 = []
	
	# generate weights from a gaussian with mu = 3.0 and sigma = 1.0. Constrain w_i >= 0. 
	w_0 = [random.gauss(3.0,1.0) for i in range(NUM_NEURONS)] # at each of the 20 simulations, this is drawn 	
	#tmp_w0 = copy.deepcopy(w_0) # reassignment of list would create shallow copies!!
	theta_0 = 2.5
	f = open("weights_for_expt%d_t%d"%(experiment,TIME_LIMIT),'wt')
	f_theta = open("theta_for_expt%d_t%d"%(experiment,TIME_LIMIT),'wt')
	f_y = open("response_for_expt%d_t%d"%(experiment,TIME_LIMIT),'wt')
	f_F = open("objective_for_expt%d_t%d"%(experiment,TIME_LIMIT),'wt')	
	for t in range(TIME_LIMIT):
		pattern_index = random.randint(0,4)
		mu_j = mu[pattern_index]
		
	
		x = [constant*math.exp(-(float(i+1)-mu_j)**2/sigma**2) for i in range(NUM_NEURONS)]
		y = sum([wi*xi for wi,xi in zip(w_0,x)])
		y2 = y**2
			
		for neuron in range(NUM_NEURONS):
			
			dw = eta*x[neuron]*(y2-(theta_0*y))
		
			w_0[neuron] +=  dw 
			if w_0[neuron] < 0:
				w_0[neuron] = 0.0
				 
		
			if (t % 1000) == 0:
				print "time: ",t

		y = sum([wi*xi for wi,xi in zip(w_0,x)])
		f_y.write(str("%lf\n"%y))
				
		y2= y**2

		dtheta=  (1.0/tau)*(y2-theta_0)
		theta_0 += dtheta
		f_theta.write(str("%lf\n"%theta_0))
		
		sig2_y = (sig2_y*(float(t)/(t+1.0))) + ((1/(t+1.0))*y2) #running average
		sig_y = math.sqrt(sig2_y)
		F = ((float(t)/(t+1.0)) * F) + ((1.0/(t+1.0)) * (y/sig_y)**3)
		f_F.write(str("%lf\n"%F))

	for i in range(NUM_NEURONS):
		f.write(str("%lf\n"%w_0[i]))
	f.close()
	f_theta.close()
	f_y.close()
	f_F.close()

