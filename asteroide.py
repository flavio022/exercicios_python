import math

class TAsteroide:
    def __init__(self,x,y,raio):
        self.x = x
        self.y = y
        self.raio = raio

class TPonto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def colideAsteroide(asteroide,ponto):
    distancia = abs(math.sqrt(  (ponto.x - asteroide.x)**2 + (ponto.y - asteroide.y)**2 ))

    print(distancia)
    
    if(distancia <= asteroide.raio):
        print("Colidiu")
    else:
        print("Não colidiu")

ast = TAsteroide(1,2,3)
ponto = TPonto(1,1)

print(colideAsteroide(ast,ponto))
