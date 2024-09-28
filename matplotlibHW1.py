#Develop a choice based program where the user inputs the type of equation
# (linear, quadratic and cubic (optional)) and take the coefficients as input and plot the graph for them for range x = 0 to x = 50. 

import matplotlib.pyplot as plt
import numpy as np

def plot_graph(y, x, equationType):
    plt.plot(x, y, label = equationType)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.legend()
    plt.title(f"{equationType} Equation")
    plt.show()

def main():
    print("Choose the type of equation: ")
    print("1. Linear (y = ax + b)")
    print("2. Quadratic (y = (ax)^2 + bx + c")
    print("3. Cubic (y = (ax)^3 + (bx)^2 + cx + d")
    choice = int(input("Enter your choice 1, 2, or 3: "))

    #creates an evenly spaced numbers - range of numbers
    x = np.linspace(0, 50, 500)

    if choice == 1:
        print("You chose linear equation")
        a = float(input("Enter the coefficient a: "))
        b = float(input("Enter the coefficient b: "))
        y = (a * x) + b
        plot_graph(x, y, "linear")

    if choice == 2:
        print("You chose quadratic equation")
        a = float(input("Enter the coefficient a: "))
        b = float(input("Enter the coefficent b: "))
        c = float(input("Enter the coefficent c: "))
        y = (a*x**2) + (b*x) + c
        plot_graph(x, y, "quadratic")

    if choice == 3:
        print("You chose cubic equation")
        a = float(input("Enter the coefficient a: "))
        b = float(input("Enter the coefficient b: "))
        c = float(input("Enter the coefficient c: "))
        d = float(input("Enter the coefficient d: "))
        y = (a*x**3) + (b*x**2) + (c*x) + d
        plot_graph(x, y, "cubic")

    else:
        print("Invalid Choice! Please Run the Program Again!")
    
main()

'''
#linspace
arr = np.linspace(0, 20, 5)
print(arr)
'''