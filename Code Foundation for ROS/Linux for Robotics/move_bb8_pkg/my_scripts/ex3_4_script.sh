#/bin/bash

ARG1=$1

if [ $ARG1 == "circle" ]; then
    echo "cycling.."
    rosrun move_bb8_pkg move_bb8_circle.py

elif [ $ARG1 == "forward_backward" ]; then
    echo "fowrward and backward.."
    rosrun move_bb8_pkg move_bb8_

elif [ $ARG1 == "square" ]; then
    echo "squaring.."
    rosrun move_bb8_pkg move_bb8_square.py

else 
echo "Please enter one of the following;
circle
forward_backward
square"

fi