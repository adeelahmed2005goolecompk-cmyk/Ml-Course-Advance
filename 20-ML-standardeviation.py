# Theory about this code:

# This code demonstrates how to calculate the population standard deviation
# using NumPy. First, the numpy library is imported as np, which provides
# mathematical and statistical functions for numerical data.
# The data list contains five numerical values: 10, 12, 14, 16, and 18.
# The np.std(data) function is used to calculate the standard deviation of these values.
# Standard deviation measures how much the data values vary or spread out from their mean.
# Since np.std() uses the population standard deviation by default, the calculation
# considers the entire dataset as the population. The calculated standard deviation
# is stored in the variable standard_deviation. Finally, print(standard_deviation)
# displays the result. For this dataset, the population standard deviation is
# approximately 2.83. Overall, this code shows how NumPy can be used to easily
# calculate the spread and variability of numerical data.





#pip install numpy

import numpy as np

data = [10, 12, 14, 16, 18]

# Population standard deviation

standard_deviation = np.std(data)
print(standard_deviation)

