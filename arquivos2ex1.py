import random
m =[[],[],[],[],[]]
for i in range(5):
    m[0].append(random.randint(0,50))
    m[1].append(random.randint(0,50))
    m[2].append(random.randint(0,50))
    m[3].append(random.randint(0,50))
    m[4].append(random.randint(0,50))
print(m)
#soma da linha 4
soma = 0
for i in range(len(m[3])):
    soma += m[3][i]
print("Soma da linha 4 = ", soma)
print()
#Soma da coluna 2
soma = 0
for i in range(len(m)):
    soma += m[i][1]
print("A soma da coluna 2 = ", soma)
print()
#Soma da diagonal principal
soma = 0
for i in range(len(m)):
    soma +=m[i][i]
print("Soma da diagonal principal = ", soma)
print()
#Soma da diagonal secundária
soma = 0
for i in range(len(m)):
    soma += m[i][len(m)-1-i]
print("Soma da diagonal secundária = ", soma)
print()
#Soma de todos os elementos
soma = 0
for i in range(len(m)):
    for  j in range(len(m[i])):
        soma += m[i][j]
print("Soma de todos os elementos = ", soma)

             

