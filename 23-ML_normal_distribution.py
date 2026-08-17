# Theory about this code:

# This code demonstrates how to create a histogram using NumPy and Matplotlib.
# First, the numpy library is imported for numerical operations,
# and matplotlib.pyplot is imported as plt for data visualization.
# The numpy.random.normal(5.0, 1.0, 100000) function generates 100,000 random values
# following a normal distribution with a mean of 5.0 and a standard deviation of
# 1.0. However, the generated data is immediately replaced by the tuple (1,2,3,4,5,6,7,8,9),
# so the random data is not actually used in the histogram. The print(x) statement
# displays the tuple values in the console. The plt.hist(x, 100) function creates
# a histogram using the values in x and divides the range into 100 bins. Since there
# are only nine values, many bins will contain no data. Finally, plt.show() displays
# the histogram. Overall, the code demonstrates the basic concept of generating
# numerical data and visualizing its distribution with a histogram, although
# the random data line should not be overwritten if the intention is to visualize
# the normal distribution.




import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

x = (1,2,3,4,5,6,7,8,9)
print(x)
plt.hist(x, 100)
plt.show()