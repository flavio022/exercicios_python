lista1 = [1,2,3]
lista2 = [2,3,4]

for i in range(len(lista1)):
    for j in range(i-1,len(lista2)):
        print(lista1[i],'x', lista2[j])
