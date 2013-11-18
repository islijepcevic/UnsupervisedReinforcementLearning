import math 
import random 
random.seed(0)

eta = 5.0*(10**(-2))
tau = 1.0*(10**(2))
dt = 1.0
x_0 =  1.0
theta_0 = 2.5
sigma = 10.0
constant = 1/math.sqrt(2*math.pi*(sigma**2))

mu = []
x = [] #[[constant*math.exp(-(i-mu[j])**2/sigma**2) for i in range(1,101)] for j in range(5)]
y = [] #[w*x for w,x in zip(omega_0,x[j])] for j in range(5) ]
y2 = [] #[[y*y for y,y in zip(y[j],y[j])] for j in range(5) ] #y2 = [sum(y2[j]) for j in range(5)]

for experiment in range(20): #simulate the paradigm using many different initializations of w_0
	omega_0 = [random.gauss(3.0,1.0) for i in range(100)] # at each of the 20 simulations, this is drawn 
	#from a gaussian with mu = 3.0 and sigma = 1.0. Constrain w_i >= 0. 
	for j in range(5):
		mu.append((20*j)+10)
		x.append([constant*math.exp(-(i-mu[j])**2/sigma**2) for i in range(1,101)])
		y.append(sum([w*x for w,x in zip(omega_0,x[j])]))
		y2.append(y[j]**2)
		for neuron in range(100): # can i avoid this using list comprehensions? also how to update y and y2??
			for t in range(100):
				theta_0[neuron] += (1.0/tau)*(y2[j]-theta_0[neuron])
				omega_0[neuron] += eta*x[j]*(y2[j]-theta_0[neuron]) #careful of the difference between time t and input neuron number i

print mu
print x[4][97] #index for i = n is n-1 because array indexing starts from zero while neuron nums start from one	
