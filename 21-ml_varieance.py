# Theory about this code:


# This code demonstrates how to calculate the variance of numerical data using NumPy.
# First, the numpy library is imported, which provides mathematical and statistical
# functions for working with numerical data. The speed list contains several numerical
# values representing speed measurements. The numpy.var(speed) function calculates the
# variance of these values and stores the result in the variable x. Variance measures
# how far the data values are spread out from their mean. A higher variance indicates
# that the values are more widely distributed, while a lower variance means the values
# are closer to the average. Finally, print(x) displays the calculated variance.
# For this dataset, the variance is approximately 1432.82. Overall, this code
# demonstrates how NumPy can be used to measure the variation and spread of numerical data.




import numpy

speed = [32,111,138,28,59,77,97]

x = numpy.var(speed)

print(x)