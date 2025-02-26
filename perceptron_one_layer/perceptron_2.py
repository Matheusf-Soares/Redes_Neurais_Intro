from typing import List
import numpy as np
from numpy import ndarray

entradas = np.array([-1, 7, 5])
pesos = np.array([.8, .1, .0])

def soma(e: ndarray, p: ndarray) -> float:
    return e.dot(p)
# dot product -> produto escalar

s = soma(entradas, pesos)

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

r = stepFunction(s)
r
