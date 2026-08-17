# Theory-About-This-Code:


# This code demonstrates how to create scatter plots using Matplotlib.
# First, matplotlib.pyplot is imported as plt, which provides functions
# for creating graphs. The first section is commented out, so it does not execute;
# it shows an example of plotting value1 and value2 using plt.scatter().
# The print() statement is used to display a separator in the console.
# In the next section, week1 contains values from 1 to 7 representing days of a week,
# while speed_1 contains corresponding speed values. Similarly,
# week2 contains the same week values and speed_2 contains another set of speed values.
# plt.scatter(week1, speed_1) creates a scatter plot for the first dataset,
# while plt.scatter(week2, speed_2) adds the second dataset to the same graph.
# plt.show() displays both datasets together, allowing us to compare their speed
# values across the week. The second section creates three datasets named data1, data2,
# and data3, along with an age dataset. Three separate plt.scatter()
# commands are used to plot each dataset against the same age values.
# This allows us to compare three different groups of data according to age.
# Overall, the code explains how scatter plots can be used to visualize relationships,
# compare multiple datasets, and identify patterns between numerical values.





import matplotlib.pyplot as plt


#value1 = (1,2,3,4,5,6)


#value2 = (1,2,3,4,5,60)

#plt.scatter(value1, value2)

#plt.show()



print("##################################")

week1= (1, 2, 3, 4, 5 ,6, 7)
speed_1 = (20, 30, 40, 50 , 60 ,70 ,  80)

week2= (1, 2, 3, 4, 5 ,6, 7)
speed_2 = (10, 20, 30, 40, 50 , 60, 70)

plt.scatter(week1, speed_1)

plt.scatter(week2, speed_2)

plt.show()




print("##################################")


data1 = (50,60, 70, 76, 68)

data2 = (20, 10, 24, 22, 14)

data3 = (90,99, 98, 95,96)

age = (18, 19, 20,17, 16)



plt.scatter(data1,age )
plt.scatter(data2, age)
plt.scatter(data3, age)

plt.show()















#print("befor show")

#plt.show()

#print("after show")