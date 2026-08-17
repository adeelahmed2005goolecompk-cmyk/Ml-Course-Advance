# Theory-about-this-code:

# This Python program demonstrates creating and customizing a line graph
# using Matplotlib. Two sets of numerical values, value1 and value2,
# are created and used as the x-axis and y-axis data.
# The plt.plot() function connects the values with a solid line.
# The plt.xlabel() and plt.ylabel() functions add labels to both axes,
# making the graph easier to understand. The plt.
# title() function adds the title "Graph" and places it on the right side of the graph
# using loc="right". Finally, plt.show() displays the completed graph.



import matplotlib.pyplot as plt


value1 = (11,2,3,4,5,6)


value2 = (1,2,3,4,5,60)

plt.plot(value1, value2, "-")


plt.xlabel("values of value1")


plt.ylabel("values of value2")
plt.title("Graph", loc = 'right')

plt.show()




















#print("befor show")

#plt.show()

#print("after show")