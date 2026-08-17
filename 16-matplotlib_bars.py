# Theor of this code:

# This code demonstrates how to create a vertical bar chart using Matplotlib.
# The matplotlib.pyplot module is imported as plt to provide the functions needed
# for creating and displaying the graph. value1 contains the values from
# 1 to 10 and is used for the x-axis, while value2 contains the corresponding
# values that determine the height of each bar. The plt.bar(value1, value2)
# function creates a vertical bar chart where each value in value1 represents
# the position of a bar and the corresponding value in value2 determines its height.
# The color="#00FFFF" argument changes the color of all bars to cyan.
# The plt.bar() function is used for vertical bars,
# while plt.barh() is used to create horizontal bars.
# Bar charts are useful for comparing different numerical
# values and clearly showing differences between categories.
# The plt.show() function displays the completed chart.
# The height parameter is used with plt.bar() to control bar heights;
# for horizontal bars, plt.barh() uses width to control the horizontal
# length of the bars. Overall, this code explains the basic concept of
# creating and customizing bar charts for data comparison.






import matplotlib.pyplot as plt


value1 = (1,2,3,4,5,6,7,8,9,10)


value2 = (1,2,3,4,5,60,70, 80, 90, 100)



# plt.bar(value1,value2, color = "color_name", width = size of width of bars)

plt.bar(value1,value2, color = "#00FFFF")  # plt.barh() is used for horizontal plot and plt.bar() vertical plot
plt.show()


note:- height = tell height of bars bwtween 0 and 1 and it is only used in horizontal bars
