import random
lista = []
for i in range(20):
    lista.append(random.randint(-50,50))
lista2 = [c for c in lista if c >0]
print (lista,lista2)
