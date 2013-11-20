import matplotlib
import matplotlib.pyplot as plt 
import math
import pylab 
TIME_LIMIT = 10000
NUM_EXPTS = 1

for expt in range(NUM_EXPTS):
	data = [[float(line)  for line in open("weights%d_t%d_expt%d" %(i ,TIME_LIMIT, expt))] for i in range(5)]

	colors = ['red', 'green', 'blue', 'yellow',  'black']
	fig = pylab.figure()
	for i in range(5):	
		pylab.plot(data[i], color=colors[i],linewidth=1.0,label="$\mu_j$ = %d"%(20*i+10))
		pylab.hold(True)
	fig.suptitle('Run: %d after t = %d'%(expt,TIME_LIMIT), fontsize=14)
	pylab.legend(loc='upper left',prop={'size':10})
	pylab.savefig("weights_expt%d_t%d_results.png"%(expt,TIME_LIMIT))

