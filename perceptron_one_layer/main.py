from typing import List

entradas: List[int] = [-1, 7, 5]
pesos: List[float] = [.8, .1, .0]

def soma(e, p):
    s = 0
    for i in range(len(entradas)):
        s += e[i] * p[i]
    return s

s = soma(entradas, pesos)

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

r = stepFunction(s)

