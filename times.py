"""meu_arquivo = open('arquivos.txt', 'r')
linha = meu_arquivo.readline()
time_a = linha.rstrip()
linha = meu_arquivo.readline()
time_b = linha.rstrip()

print('Jogo:')
print(time_a,'versus',time_b)
print("Não perca esse evento!")

meu_arquivo.close()"""

final_arquivo = False
string_vazia = ''
meu_arquivo = open('arquivos.txt', 'r')

print('Times que participarão deste campeonato: ')
while not final_arquivo:
    linha = meu_arquivo.readline()
    if linha == string_vazia:
        final_arquivo = True
    else:
        time = linha.rstrip()
        print('-',time)
meu_arquivo.close()

