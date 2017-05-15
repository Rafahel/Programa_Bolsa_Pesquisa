from numpy import *
from scipy.interpolate import *


def geradorPolinomio(x, y):
    polinomio = polyfit(x, y, 3)
    xA = float(polinomio[0])
    xB = float(polinomio[1])
    xC = float(polinomio[2])
    xD = float(polinomio[3])
    formula = "f(x) = (" + str(xA) + " * x3) + (" + str(xB) + " * x2) + (" + str(xC) + " * x) + (" + str(xD) + ")"
    print(xD)
    return formula