import math 
import random 
random.seed(0)

NUM_NEURONS = 100
TIME_LIMIT = 50000
MU_RANGE = 5
NUM_EXPTS = 30
eta = 5.0*(10**(-2))
tau = 1.0*(10**(2))
dt = 1.0
x_0 =  1.0


sigma = 10.0
constant = 1.0/math.sqrt(2*math.pi*(sigma**2))



for experiment in range(NUM_EXPTS): #simulate the paradigm using many different initializations of w_0
	mu = []
	y = []
	y2 = []
	# from a gaussian with mu = 3.0 and sigma = 1.0. Constrain w_i >= 0. 
	w_0 = [random.gauss(3.0,1.0) for i in range(NUM_NEURONS)] # at each of the 20 simulations, this is drawn 
	
	tmp_w0 = w_0
	for j in range(MU_RANGE):
		w_0 = tmp_w0 # use the same weights for all inputs
		f = open("weights%d_t%d_expt%d"%(j ,TIME_LIMIT, experiment),'wt')
		theta_0 = [2.5 for i in range(MU_RANGE)] 
		#print theta_0
		mu.append((20.0*j)+10.0) # append a new input pattern to train the neural network
		x = [constant*math.exp(-(float(i+1)-mu[j])**2/sigma**2) for i in range(NUM_NEURONS)]
		#print x
		y.append(sum([wi*xi for wi,xi in zip(w_0,x)]))
		y2.append(y[j]**2)
		
		for neuron in range(NUM_NEURONS):
			
			dw =  "inf"
			dtheta = "inf"

			print x
			for t in range(TIME_LIMIT): # what is convergence?
				dtheta=  (1.0/tau)*(y2[j]-theta_0[j])
				dw = eta*x[neuron]*(y2[j]-(theta_0[j]*y[j]))
				#print "delta_theta: ",dtheta, " delta_w: " , dw
				w_0[neuron] +=  dw 
				if w_0[neuron] < 0:
					print "negative weight"
					break
				theta_0[j] += dtheta
				 
				#print "w0:",w_0[neuron],"x:",x
				if (t % 1000) == 0:
					print "time: ",t	
			f.write(str("%lf\n"%w_0[neuron]))
		f.close()	
		y[j] = sum([wi*xi for wi,xi in zip(w_0,x)])
		y2[j] = y[j]**2
	

'''	#f_weights = open("data/weights_expt%d"%experiment,'wt')
	#f_thetas = open("data/theta_expt%d"%experiment,'wt')
	#f_outputs = open("data/outputs_expt%d"%experiment,'wt') '''
