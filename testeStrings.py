nome = input('Nome completo:')
nomes = nome.split(' ')
iniciais = ''
for n in nomes:
     if not n in ('e', 'do', 'da', 'dos', 'das', 'de', 'di', 'du'):
         iniciais += n[0].upper()
print(iniciais)



#Criar uma nova string onde “not “ seja adicionado na frente de texto. Se o texto informado já
#iniciar com “not”, não criar uma nova string. Exibir resultado.
texto = input("Digite um texto/string")
var = "NOT"
if not var in texto:
    textoat = var+texto
    print(textoat)
else:
    print(texto)
#Criar uma nova string onde a primeira letra do texto informado seja trocada pela última letra do
#mesmo. Exibir resultado
texto2 = input('Digite um texto/string: ')
texto2 = texto2[len(texto2)-1] + texto2[1:len(texto2)-1] + texto2[0]
print(texto2)
#Criar uma nova string com o texto informado e com seu último caractere adicionado no início e no
texto = input("Digite uma string")
texto = texto[len(texto)-1]+texto+texto[len(texto)-1]
print(texto)
texto = input("Digite uma string")
if "hi" in texto:
    print("SIM")
else:
    print("Não")
texto = input("Digite uma string")
posicao = texto.find('del')
if posicao <1:
    print("string original")
else:
    print(texto[:posicao]+texto[posicao+3:])

texto = input("Digite uma string")
if 
import random

while True:
    palpite = input('Qual é o seu palpite para a face do dado? ')
    if palpite.isalpha():
        print("Apenas numeros")
    else:
        face = random.randint(1,6)
        if int(palpite) == face:
            print('Você acertou,O valor da face do dado foi', face)
        else:
           print('Você errou. O valor da face do dado foi', face)
    jogar = input("Jogar de novo? [s/n]")
    if jogar == 'n':
        print("Ate logo!")
        break
   
