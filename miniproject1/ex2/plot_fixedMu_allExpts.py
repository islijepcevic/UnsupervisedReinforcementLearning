import matplotlib
import matplotlib.pyplot as plt 
import math
import pylab 
TIME_LIMIT = 50000
NUM_EXPTS = 30
NUM_INPUTS = 5 # num of input patterns

for oneInput in range(NUM_INPUTS):
	data = [[float(line)  for line in open("weights%d_t%d_expt%d" %(oneInput ,TIME_LIMIT, i))] for i in range(NUM_EXPTS)] 
	#load data in data[expt][neuron] format for given sim length
	colors = ['red', 'green', 'blue', 'yellow',  'black']
	fig = pylab.figure()
	mean = [pylab.mean([data[expt][neuron] for expt in range(NUM_EXPTS)]) for neuron in range(len(data[0]))]
	for expt in range(NUM_EXPTS):	
		pylab.plot(mean, color='red',linewidth=1.0)
		pylab.hold(True)
	fig.suptitle('Mean response to $\mu_j$ = %d after t = %d, average of %d'%(20*oneInput+10,TIME_LIMIT,NUM_EXPTS), fontsize=14)
	#pylab.legend(loc='upper left',prop={'size':10})
	pylab.savefig("weights_mu%d_t%d_allExpts_mean_results.png"%(20*oneInput+10,TIME_LIMIT))

