

This Python program demonstrates creating a point graph and customizing it
using Matplotlib. Two sets of numerical values, value1 and value2,
are used as the x-axis and y-axis data. The plt.plot() function
with the "o" marker displays the values as individual points.
Labels are added to both axes using plt.xlabel() and plt.ylabel(),
while plt.title() adds the title "Graph" and places it on the right side.
The program also demonstrates how to add a grid to the graph.
The grid can be displayed on both axes or only on the x-axis or y-axis.
In the active code, the grid is customized with a green color,
dashed line style, and a linewidth of 0.5. Finally, plt.show()
displays the complete graph.






import matplotlib.pyplot as plt


value1 = (1,2,3,4,5,6)


value2 = (1,2,3,4,5,60)

plt.plot(value1, value2, "o")

# add label to x 
plt.xlabel("values of value1")


#add label to y
plt.ylabel("values of value2")

# add title to plot
plt.title("Graph", loc = 'right')


# add grid to plot
# plt.grid()
#
# plt.grid(axis = 'x')   # show only x axis grid

# plt.grid(axis = 'y')	# show only y axis grid

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()

print("befor show")

plt.show()

print("after show")