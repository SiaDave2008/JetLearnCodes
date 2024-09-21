#Data vis: A way to analyze numerical data through graphs
# Line graphs
# Bar graphs
# Scatter plot
#Bivariate Analysis: 2 features analysis

import matplotlib.pyplot as plt
import numpy as np

'''
x = [1,2,3,4,5]
y = [1,2,3,4,5]
                                    #thickness of the line
plt.plot(x, y, "g--", label = "y = x", linewidth = 4)
        #     (x     |      y)
        #[start, end, start, end]
plt.axis([0,10,0,50])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("testGraph")
#show label
plt.legend()
plt.show()
'''

#Plot multi graphs on single plot
'''
plt.plot([1,2,3,4,5], [1,4,9,16,25], "r--", label = "y = √x", linewidth = 5)
plt.plot([1,2,3,4,5], [1, 8, 27, 64, 125], "b--", label = "y = 3√x", linewidth = 3)
plt.axis([0, 10, 0, 150])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Squares + Cubes")
plt.legend()
plt.show()
'''

'''
x = np.arange(0, 10, 0.2)
print(x)

y1 = x**2, y2 = x**3

plt.plot(x, y1, "g--", x, y2, "b--")
plt.show()
'''

#task: plotting a line using user input, y = mx + c
'''
m = int(input("Enter the slope: "))
c = int(input("Enter the intercept: "))
x = np.arange(0, 10, 1)
y = (m*x) + c

plt.plot(x, y, label = "y = mx + c")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.title("Line Equation")
plt.show()
'''

# plt.bar([1,3,5,7], [2,6,4,9], color = "b")
# plt.bar([2,4,6,8], [3,5,7,9], color = "g")
plt.bar(["Male Literacy", "Female Literacy"], [90, 95])
plt.show()
