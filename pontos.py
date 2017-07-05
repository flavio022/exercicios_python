import math

def hipotenusa(x,y):
    cateto1 = x**2
    cateto2 = y**2
    soma = cateto1 + cateto2
    hipo = math.sqrt(soma)
    return hipo

def distancia(x,y):
    c1 = y[0] - x[0]
    c2 = y[1] - x[1]
    hipot = hipotenusa(c1,c2)
    return hipot
    

arquivo_entrada = open("pontos.txt","r")
arquivo_saida = open("distancias.txt","w")
pontos1=[]
pontos2=[]
for linha in arquivo_entrada:
    pontos = linha.strip().split(":")
    pt1 = pontos[0]
    pt2 = pontos[1]
    pt3 = pontos[2]
    pontos1.append(float(pt2))
    pontos2.append(float(pt3))

    
print(distancia(pontos1,pontos2))

