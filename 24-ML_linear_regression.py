#Theory about this code

This code demonstrates how to create a scatter plot using Matplotlib. First, the matplotlib.
pyplot library is imported as plt, which provides functions for creating graphs and visualizing data.
The x list contains numerical values that represent the x-axis, while the y list contains corresponding
numerical values that represent the y-axis. The plt.scatter(x, y) function creates a scatter plot by placing
each pair of values (x, y) as an individual point on the graph. Each point represents the relationship between
the corresponding values from the two lists. Scatter plots are useful for identifying patterns, relationships,
trends, and variations between two numerical variables. Finally, plt.show() displays the scatter plot on the screen. 
Overall, this code provides a simple example of using a scatter plot to visualize the relationship between two sets of numerical data.




import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()