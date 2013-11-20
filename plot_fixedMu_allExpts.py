import matplotlib
import matplotlib.pyplot as plt 
import math
import pylab 
TIME_LIMIT = 50000
NUM_EXPTS = 30
NUM_INPUTS = 5 # num of input patterns
oneInput = 4

data = [[float(line)  for line in open("weights_for_mu%d_expt%d_t%d" %(oneInput , i,TIME_LIMIT))] for i in range(NUM_EXPTS)] 
#load data in data[expt][neuron] format for given sim length
colors = ['red', 'green', 'blue', 'yellow',  'black']
fig = pylab.figure()
mean = [pylab.mean([data[expt][neuron] for expt in range(NUM_EXPTS)]) for neuron in range(len(data[0]))]
for expt in range(NUM_EXPTS):	
	pylab.plot(mean, color='red',linewidth=1.0)
	pylab.hold(True)
fig.suptitle('Mean response after t = %d, average of %d'%(TIME_LIMIT,NUM_EXPTS), fontsize=14)
#pylab.legend(loc='upper left',prop={'size':10})
pylab.savefig("weights_t%d_mean_results.png"%(TIME_LIMIT))

