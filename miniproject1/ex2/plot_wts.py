import matplotlib
import matplotlib.pyplot as plt 
import math
import pylab 
import cst_sim as cs

data = [[float(line)  for line in open("weights_for_expt%d_t%d" %(i,cs.TIME_LIMIT))] for i in range(cs.NUM_EXPTS)] 
#print len(data[0])
#load data in data[expt][neuron] format for given sim length
colors = ['red', 'green', 'blue', 'yellow',  'black']
fig = pylab.figure()
mean = [pylab.mean([data[expt][neuron] for expt in range(cs.NUM_EXPTS)]) for neuron in range(len(data[0]))]
	
pylab.plot(mean, color='red',linewidth=1.0)
pylab.hold(True)
fig.suptitle('Mean response after t = %d, average of %d'%(cs.TIME_LIMIT,cs.NUM_EXPTS), fontsize=14)
#pylab.legend(loc='upper left',prop={'size':10})
pylab.savefig("weights_t%d_mean_results.png"%(cs.TIME_LIMIT))

