# Theory-About-This-Code:

# This Python program demonstrates data visualization using Matplotlib,
# mainly for identifying patterns and possible outliers in data.
# First, the Matplotlib library is imported and its installed version is displayed.
# The pyplot module is then imported for creating graphs.
# Two sets of numerical values, x and y, are created, where the last
# value in x is significantly larger than the other values.
# The plt.plot(x, y) function creates a line plot using these values.
# Finally, plt.show() displays the graph. This type of visualization can help
# understand data patterns and identify unusual or extreme values
# that may represent outliers.







#matplotlib
#why ploting (outlier detection)


import matplotlib

# print version of matplotlib
print(matplotlib.__version__)

print("################################# ploting ##########################")



import matplotlib.pyplot as plt


x = (1,2,3,4,5,6,7,8,9, 50)


y = (1,2,3,4,5,6,7,8,9, 5)

plt.plot(x, y)



plt.show()
