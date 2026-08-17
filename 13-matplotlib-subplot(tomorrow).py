# Theory-About-This-Code:

# This code demonstrates the basic use of Matplotlib for creating multiple plots using subplot().
# import matplotlib.pyplot as plt imports Matplotlib's plotting module.
# value1, value2, and value3 are tuples containing numerical values that can be used for plotting.
# plt.subplot(1, 2, 1) creates a subplot layout with 1 row and 2 columns and selects the first subplot.
# The first value 1 represents the number of rows.
# The second value 2 represents the number of columns.
# The third value 1 represents the position of the current subplot.
# plt.show() displays the created figure on the screen.
# Since no plotting function such as plt.plot() is used, the subplot area will appear empty.
# The commented print() statements demonstrate that Python executes statements before and after plt.show().
# plt.show() is mainly used to display the Matplotlib figure.
# The three value sets could later be used to create different graphs.
# For example, value1 and value2 could be plotted as line graphs.
# value3 contains larger values and could be used for another comparison.
# Subplots are useful when you want to display multiple graphs in one figure.
# Overall, this code provides a basic introduction to Matplotlib subplots and displaying figures.





import matplotlib.pyplot as plt


value1 = (1,2,3,4,5,6)


value2 = (1,2,3,4,5,60)

value3  = (11,22,33,44,55,66)




plt.subplot(1, 2, 1)
plt.show()




















#print("befor show")

#plt.show()

#print("after show")