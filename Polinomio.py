from numpy import *
from scipy.interpolate import  *


def geradorPolinomio(x, y):
    polinomio = polyfit(x, y, 2)
    xA = float(polinomio[0])
    xB = float(polinomio[1])
    xC = float(polinomio[2])
    formula = "f(x) = (" + str(xA) + " * x1) + (" + str(xB) + " * x2) + (" + str(xC) + ")"
    # print(formula)
    return formula