#!/bin/bash

REPEATS=5
TIME=`date +%m_%d_%H_%M`
FILE="data_${TIME}.out"

for i in {1..5}; do
    python main.py >> $FILE
done

python plotter.py $FILE
