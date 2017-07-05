"""Plano cartesiano"""

import math

def hipotenusa(x,y):
    cateto1 = x**2
    cateto2 = y**2
    soma = cateto1 + cateto2
    hipo = math.sqrt(soma)
    return hipo
def distancia(x,y):
    c1 = y[0]- x[0]
    c2 = y[1]- x[1]
    hipot = hipotenusa(c1,c2)
    return hipot
def main():
    
    p1 = (5.5, 7.5)
    p2 = (5.22,4.22)
    print("A distância entre os pontos é :", distancia(p1,p2))

main()
x
