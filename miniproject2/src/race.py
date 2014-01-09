from pylab import *
import params
import car
import track
import params

import numpy as np
from plotter import *
import neural_network as nn
ion()

# This function trains a car in a track. 
# Your car.py class should be able to be accessed in this way.
# You may call this file by:

# import race
# final_car = race.train_car()
# race.show_race(final_car)

def train_car(save_learning_curve = False):
    
    close('all')
    
    # create instances of a car and a track
    monaco = track.track()
    ferrari = car.car()
        
    n_trials = 1000
    n_time_steps = 1000 # maximum time steps for each trial

    if save_learning_curve:
        learn_curve_file = open(params.LEARNING_CURVE_FILE, 'a')
    
    '''    
    net = nn.NeuralNetwork(params.POS_NEURONS, params.POS_RANGE, 
                params.VEL_NEURONS, params.STATIC_VEL_RANGE, params.NB_OUTPUTS, 
                params.ETA, params.GAMMA, params.LAMBDA)
    '''
    for j in arange(n_trials):	

        # before every trial, reset the track and the car.
        # the track setup returns the initial position and velocity. 
        (position_0, velocity_0) = monaco.setup()	
        ferrari.reset()
        
        # choose a first action
        action = ferrari.choose_action(position_0, velocity_0, 0)
        
        # iterate over time
        for i in arange(n_time_steps) :	
            
            # the track receives which action was taken and 
            # returns the new position and velocity, and the reward value.
            (position, velocity, R) = monaco.move(action)	

            # the car chooses a new action based on the new states and reward,
            # and updates its parameters
            action = ferrari.choose_action(position, velocity, R)	
            
            # check if the race is over
            if monaco.finished is True:
                break
        else:
            print "Did not finish the track"
            print "Total reward:", monaco.total_reward

        if save_learning_curve:
            print >> learn_curve_file, \
                    j, monaco.time, monaco.total_reward, monaco.finished
        
        if j%100 == 0 and not save_learning_curve:
            # plots the race result every 100 trials
            monaco.plot_world()
            
        if j%10 == 0:
            print
            print 'TRIAL:', j

        # uncomment only when plotting navigation maps
        #if (j+1)%100 == 0:
        #    plot_navigation_map(ferrari, j+1)

    if save_learning_curve:
        learn_curve_file.close()

    return ferrari #returns a trained car
    
# This function shows a race of a trained car, with learning turned off
def show_race(ferrari):

    close('all')

    # create instances of a track
    monaco = track.track()

    n_time_steps = 1000  # maximum time steps
    
    # choose to plot every step and start from defined position
    (position_0, velocity_0) = monaco.setup(plotting=True)	
    ferrari.reset()

    # choose a first action
    action = ferrari.choose_action(position_0, velocity_0, 0)

    # iterate over time
    for i in arange(n_time_steps) :	

        # inform your action
        (position, velocity, R) = monaco.move(action)	

        # choose new action, with learning turned off
        action = ferrari.choose_action(position, velocity, R, learn=False)	

        # check if the race is over
        if monaco.finished is True:
            break


    print "finished"
    raw_input()

