#Build a choice based program 
# where the user will give the input for 
# the type of equation (Linear / Quadratic) 
# and take inputs for coefficients accordingly. 
# Display the output values of the equation 
# for x = 0 to x = 10.

#NumPy Homework:
import numpy as np

def linear_equation(y, x, m, b):
    print("Your linear equation is: ", y, " = ", x, "•", m, " + ", b)
    ans_y = (x*m) + b
    print("y = ", ans_y)
    ans_x = (y/m) + b
    print("x = ", ans_x)

def quadratic_equation(x, a, b, c):
    print("Your quadratic equation is: (", a, "•", x, ")^2", " + ", b, "•", x, " + ", c, " = 0")
    ans = ((a*x)*(a*x)) + (b*x) + c
    print("Answer: ", ans, " = 0")

print("Choose the type of equation: ")
user_input = input("(Linear / Quadratic) - (L / Q) ")

if user_input == "L":
    print("Choose the y, x, m, b values")
    y = int(input("Choose the y value: "))
    x = int(input("Choose the x value: "))
    m = int(input("Choose the m value: "))
    b = int(input("Choose the b value: "))
    linear_equation(y, x, m, b)

if user_input == "Q":
    print("Choose the a, b, c, x values")
    x = int(input("Choose the x value: "))
    a = int(input("Choose the a value: "))
    b = int(input("Choose the b value: "))
    c = int(input("Choose the c value: "))
    quadratic_equation(x, a, b, c)

else:
    print("invalid!")