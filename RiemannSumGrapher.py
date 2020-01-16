import numpy as np
import matplotlib.pyplot as plt
import math
# This program calculates the Riemann sum which is the area under a curve
#
# The function being used in this case is y = x^2
#
# This program integrates the function from x1 to x2
# x2 must be greater than x1, otherwise the program will print an error message.
# this program is meant to graph what the riemann_sum should look like

equation = input("Type in any equation: ")
taco_1 = int(input("X range 1: "))
taco_2 = int(input("X range 2: "))

def graph(equation, x_range):
    x = np.array(x_range)
    y = eval(equation)
    plt.plot(x, y)
    plt.show()


graph(equation, range(taco_1, taco_2))
