"""Funcção para calcular a hipotenusa de um trângulo"""

import math

def hipotenusa(x,y):
    quadrado1 = x**2
    quadrado2 = y**2
    soma = quadrado1 + quadrado2
    hipo = math.sqrt(soma)
    return hipo

n1 = float(input("Cateto 1: "))
n2 = float(input("Cateto 2: "))
print(hipotenusa(n1,n2))
