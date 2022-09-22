import math
import random
import statistics
import matplotlib.pyplot as plt
import numpy as np
# Charles Truscott Watters
# Find some theta such that theta times half of a number equals the square root of that number

def find_theta_such_that(x):
    y = round(math.sqrt(x), 4)
    z = x / 2
    high = x
    low = 0
    guess = (high + low) / 2.0
    while ((abs((round((round(abs(guess), 9) * z), 8))) - abs((round(abs(y), 8)))) >= 0.00000001):
        # Bisection Search
        if (round((round(abs(guess), 9) * z), 8) > (round(abs(y), 8))):
            high = guess
        elif (round((round(abs(guess), 9) * z), 8) < (round(abs(y), 8))):
            low = guess
        guess = (high + low) / 2.0
        theta = guess
#        print("theta times z: {}".format(round(theta * z, 0)))
#        print("theta = {} z = {} y = {} x = {}".format(round(theta, 9), z, round(y, 8), x))
#    print("Half of the square root of ten is: {}".format((0.5 * y)))
#    print("theta times half of ten is: {}".format(theta * z))
#    print("theta times two is: {}".format(2 * theta))
    theta = guess
    print("Some theta {} times {} equals the square root of {}, double {}".format(round(theta, 9), z, x, z))
    print("The square root of {} is {}. θ x (1/2)({}) = {}".format(x, math.sqrt(x), x, round(theta, 9) * ((0.5) * x)))
#    print("The square root of {} is {} and theta times half of {} is {}".format(x, y, x, round(theta, 5) * z))
    print("θ = {}".format(round(theta, 9)))
#    print("(θ * 4) ^ 2 = {}".format((theta * 4) ** 2))
#    print("(θ * 2) ^ 2 = {}".format((theta * 2) ** 2))
#    print("(θ * 3) ^ 2 = {}".format((theta * 3) ** 2))
#    print("((θ * 4) ^ 2) + ((θ * 2) ^ 2) = {}".format(round(((theta * 4) ** 2) + ((theta * 3) ** 2), 0)))
#    print("PROBLEM SOLVED: The square root of {} is {}".format(z, math.sqrt(z)))
    print("Charles Thomas Wallace Truscott Watters, thank you edX")
    print("I love you Dad. Mark William Watters. 1955 - Centurian")
    return theta

def main():
    """ Half of the square root of ten is: 1.58115
theta times half of ten is: 3.1622999999987824
theta times two is: 1.2649199999995129
Some theta 0.63246 times 5 equals the square root of 10, double 5
The square root of 10 is 3.1623 and theta times half of 10 is 3.1623
θ = 0.63246
(θ * 4) ^ 2 = 6.400090425595071
(θ * 3) ^ 2 = 3.600050864397227
((θ * 4) ^ 2) + ((θ * 2) ^ 2) = 10.0
Charles Thomas Wallace Truscott Watters, thank you edX
I love you Dad. Mark William Watters. 1955 - Centurian
Press any key to continue . . .
"""

    perfect_squares = []
    for x in range(1, 1 + 50, 1):
        perfect_squares.append(x * x)
    half_perfect_squares = []
    for square in perfect_squares:
        half_perfect_squares.append(square / 2)
    thetas = []
    for square in perfect_squares:
        thetas.append(find_theta_such_that(square))
#    plt.figure(0, figsize=[1500, 3000], dpi=np.float64(70))
#    plt.plot(list(x for x in range(1, 1 + 100, 1)), perfect_squares)
#    plt.title("Charles Truscott Watters")
#    plt.xlabel("x = One to Ten")
#    plt.ylabel("y = Perfect square of x times x")
#    plt.show()
#    plt.figure(1, figsize=[1500, 3000], dpi=np.float64(70))
#    y_inc = []
#    for x in range(1, 1 + 10, 1):
#        y_inc.append(x * 0.10)
#    for hs in half_perfect_squares:
#        y_inc.append(hs * 0.10)
#    x_also = []
#    for s in perfect_squares:
#        x_also.append(s * 0.10)
#    plt.title("Charles Truscott Watters")
#    plt.xlabel("One-tenth of half the perfect squares")
#    plt.ylabel("Some theta times half the perfect square needed to reach the square root of the perfect square")
#    plt.plot(y_inc, thetas)
#    plt.plot(y_inc, x_also)

#    plt.show()

if __name__ == "__main__": main()
