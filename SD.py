import math

import matplotlib.pyplot as plt
import random

theta = 2
m = 1000
k = 15
n = 500
graphForUni = [0] * k
graphForExpon = [0] * k


def ExponentiationAndArithmeticMean(arr, power):
    sum = 0
    for elem in arr:
        sum += (elem ** power)
    return sum / len(arr)


def draw(y, filename):
    plt.figure()
    plt.plot(range(1, k + 1), y)
    plt.savefig(filename)


for i in range(1, k + 1):
    for j in range(m):
        uniformlyDistributedRV = [0] * n
        exponentiallyDistributedRV = [0] * n
        for index in range(n):
            uniformlyDistributedRV[index] = random.uniform(0, theta)
            exponentiallyDistributedRV[index] = random.expovariate(theta)

        sumUni = ExponentiationAndArithmeticMean(uniformlyDistributedRV, i)
        sumExpon = ExponentiationAndArithmeticMean(exponentiallyDistributedRV, i)

        graphForUni[i - 1] += (((sumUni * (i + 1)) ** (1 / i) - theta) ** 2)
        graphForExpon[i - 1] += (((sumExpon / math.factorial(i)) ** (1 / i) - theta) ** 2)

    graphForUni[i - 1] /= m
    graphForExpon[i - 1] /= m

draw(graphForUni, "uniform")
draw(graphForExpon, "expon")
