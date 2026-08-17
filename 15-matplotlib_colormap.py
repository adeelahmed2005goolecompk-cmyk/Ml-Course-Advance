# TheoryAbout THIS code:

# This code demonstrates how to create a customized scatter plot using Matplotlib.
# The matplotlib.pyplot module is imported as plt to create and display the graph.
# value1 contains values from 1 to 10 and represents the x-axis values,
# while value2 contains corresponding values for the y-axis.
# The colors tuple provides different numerical values that are used to determine
# the color of each point. In plt.scatter(), the c=colors argument assigns colors
# to the points based on these values, while cmap='YlOrRd' applies the Yellow-Orange-Red
# color map. The s=8 argument controls the size of the scatter points, making every
# point small and equal in size. The comment shows that s=size could also be used to
# give each point a different size based on data. The alpha=1.0 argument controls
# transparency, where 1.0 means the points are completely visible.
# plt.colorbar() adds a color scale beside the graph to explain how the numerical
# color values correspond to the displayed colors. Finally,
# plt.show() displays the scatter plot. Overall, this code demonstrates how color,
# color maps, point size, and transparency can be used to make scatter plots more
# informative and visually meaningful.






import matplotlib.pyplot as plt


value1 = (1,2,3,4,5,6,7,8,9,10)


value2 = (1,2,3,4,5,60,70, 80, 90, 100)

colors = (0, 10, 20, 30, 40, 45 ,50,55,60,65)
size = (0, 10, 20, 30, 40, 45 ,50,55,60,65)

plt.scatter(value1, value2, c=colors, cmap='YlOrRd', s = 8 , alpha=1.0) # you may add hardcoded or use data as size : s= size

plt.colorbar()

plt.show()



