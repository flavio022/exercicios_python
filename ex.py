lista =[]

num =  int(input("Digite um número da sequência: "))

while num != - 1:
    lista.append(num)
    num =  int(input("Digite um número da sequência: "))
elemento = int(input("Digite o elemento a ser procurado: "))
cont = 0
for i in range(len(lista)):
    if lista[i] == elemento:
        cont += 1
print("O elemento %i aparece %i vezes na sequência."%(elemento, cont))

