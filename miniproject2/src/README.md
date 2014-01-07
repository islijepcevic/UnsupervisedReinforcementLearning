SOURCE DIRECTORY
================

GIVEN AND LEARNING CODE
-----------------------

`race.py` wrapper around learning algorithm, given file.

`track.py` environment for the learning agent, given file.

`car.py` our learning agent.

`neural_network.py` the neural network behind the agent.

`params.py` parameters for the algorithm.


RUNNING AND HELPING CODE
------------------------

`basic_main.py` runs learning once. Upon the end, shows the final race, or
saves the learnt agent to a file if file name given.

`learnt_main.py` shows the race with learnt agent from provided file.

`plot_learning_curve.py` plots the learning curve.

`plotter.py` contains some plotting code (mainly for debugging).


OTHER FILES
-----------

`learning_curve.data` is not part of the repository. It is generated while
running `plot_learning_curve.py` with a `-s` parameter for simulation, and it
contains data for 10 simulated cars. It is used to plot learning and reward
curves.

`plots` directory contains various plots.
