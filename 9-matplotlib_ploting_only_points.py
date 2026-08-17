# Theory About This Code:

# This Python program demonstrates plotting points using Matplotlib
# for visualizing data and identifying possible outliers.
# The program imports Matplotlib and displays its installed version.
# It then creates two sets of values, x and y, where the value 50
# in the x data is noticeably larger than the other values.
# The plt.plot(x, y, 'o') function displays the data as individual points,
# while plt.plot(x, y, "o:", ms=20) displays larger points connected with a dotted line.
# Finally, plt.show() displays the graph. This visualization
# helps observe the distribution of data and identify unusual values or possible outliers.










#matplotlib
#why ploting (outlier detection)


import matplotlib

# print version of matplotlib
print(matplotlib.__version__)

print("################################# ploting ##########################")



import matplotlib.pyplot as plt


x = (1,2,3,4,5,6,7,8,9, 50)


y = (1,2,3,4,5,6,7,8,9, 5)

plt.plot(x, y, 'o') # if you want to add * use it in quotes

plt.plot(x ,y,"o:",  ms = 20)

plt.show()


