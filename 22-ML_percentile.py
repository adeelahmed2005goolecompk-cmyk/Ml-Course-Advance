# Theory of this code:

# This code demonstrates how to calculate a percentile using NumPy.
# First, the numpy library is imported to perform numerical and statistical
# calculations. The ages list contains different age values.
# The numpy.percentile(ages, 100) function calculates the 100th percentile
# of the dataset. The 100th percentile represents the maximum value in the dataset,
# meaning it is the age below which 100% of the data values fall. In this example,
# the maximum age is 82, so the result stored in x will be 82.0. Finally,
# print(x) displays the calculated percentile. Overall, this code demonstrates
# how NumPy can be used to find the position of values within a dataset using
# percentile calculations.




import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 100)

print(x)