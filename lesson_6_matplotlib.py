import matplotlib.pyplot as plt
import numpy as np

#histogram
'''
ages = [1, 80, 43, 20, 35, 59, 7, 70, 23, 10, 89, 45, 46, 47]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

                                       #0 to 1 - relative width
plt.hist(ages, bins, histtype = "bar", rwidth = 0.8) #80%
plt.xlabel("age intervel")
plt.ylabel("frequency")
plt.show()
'''

#scatterplot
'''
hieght = [1, 2, 3, 4, 5, 6, 7, 8, 9]
weight = [0, 1, 0, 1, 0, 1, 0, 1, 0]

                                                                  #marker size or shape
plt.scatter(hieght, weight, label = "scatterplot", color = "red", marker = "o", s = 50) #s = size
plt.xlabel("hieght")
plt.ylabel("weight")
plt.title("height vs. weight")
plt.legend()
plt.show()
'''

#pie chart
'''
slices = [6, 1, 12, 1, 3]
activites = ["Sleeping", "Eating", "Working", "Workout", "Study"]
col = ["c", "m", "r", "b", "g"]

plt.pie(slices, labels = activites, colors = col, startangle = 45, shadow = True)
plt.title("Day Chart")
plt.show()
'''

#stack plot
days = [1, 2, 3, 4, 5]
eating = [2, 3, 4, 3, 2]
sleeping = [7, 8, 6, 11, 7]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 30]

plt.plot([], [], color = "m", label = "eating", linewidth = 5)
plt.plot([], [], color = "c", label = "sleeping", linewidth = 5)
plt.plot([], [], color = "r", label = "working", linewidth = 5)
plt.plot([], [], color = "g", label = "playing", linewidth = 5)

plt.stackplot(days, eating, sleeping, working, playing, colors = ["m", "c", "r", "g"])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()
