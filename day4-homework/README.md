# QBB2022 - Day 4 - Homework Exercises Submission

A. the line outputs a list of floats that decrease in sequential order by 0.05.
The numpy.arange followed by the two floats indicates we want to make a list increasing sequentially by 0.05 for each member in the list between the two floats we specify for in the range argument.
The numpy.around rounds off the floats of the list down to two decimal places, preventing in case of manipulation that the respective members of the list do not go beyond 2 decimal places in length.
[::-1] indicates we want to start counting in reverse direction.

B. as flip number increases we increase our power. However, if we use hypothesis testing correction then we require a greater number of flips to achieve the same respective power in comparison to a flip count with no correction.
