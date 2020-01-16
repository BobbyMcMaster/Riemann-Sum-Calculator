import numpy as np
import matplotlib.pyplot as plt
import math




def riemann_sum(function, a, b, num_div, right=False): #intiate paramaters
    funcobject = compile(function, "Riemann input formula", "eval") #initialize obeject
    rsum = 0
    div_size = (b - a) / num_div  # calculations the limit of the riemann_sum using iteration
    for q in range(0 + right, num_div + right):
        x = a + (q * div_size)
        func_val = eval(funcobject)
        rsum += func_val * div_size
    return rsum

def main():         # lists of prompts for user to answer to get information
    print(" Welcome to Team PKP's Riemann Sum calculator")
    print("Enter the equation as a valid Python expression")
    print("Use x as the independent variable")
    function = input("Type in an eqatuion: ")
    a = float(input("a: "))
    b = float(input("b: "))
    num_div = int(input("n: "))
    right = input("Right or left? (L/R): ").upper() == "R"
    rsum = riemann_sum(function, a, b, num_div, right)
    print(rsum)


if __name__ == "__main__":

    main()




main()
