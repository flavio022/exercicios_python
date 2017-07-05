num = int(input("Digite um número entre 1 e 23"))
votos =[]
while (num !=0 and num<24 and num>=1):
    votos.append(num)
    num = int(input("Digite um número entre 1 e 23"))
    
print("O total de votos computados é", len(votos))
print("O número e respectivos votos de todos os jogadores que receberam votos", votos)
for i in (len(votos)):
    print(i,100*votos.count(i)/n)
