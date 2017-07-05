eleitores = int(input("Qual o número de eleitores?"))
aecio = 0
dilma = 0
marina = 0
eduardo = 0
nulo = 0
branco = 0
candidato = 0
cont = 0
while cont < eleitores:
    candidato = int(input("Digite o número do candidato"))
    cont += 1
    if candidato == 45:
        aecio += 1
    elif candidato == 13:
        dilma += 1
    elif candidato == 40:
        marina += 1
    elif candidato == 43:
        eduardo += 1
    elif candidato == 1:
        nulo += 1
    elif candidato == 2:
        branco += 1
print(aecio)
print(dilma)
print(eduardo)
print(marina)
print("O total de votos nulos é " + nulo)
print("Total de votos em branco é " +branco)


            
                
                

            
                
