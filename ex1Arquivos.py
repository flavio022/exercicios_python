#Desenvolva um programa que leia os times cadastrados no arquivo arquivos.txt e apresente na tela os nomes dos times em ordem alfabetica

fim_arquivo = False
arquivo = open('arquivos.txt','r')
times=[]
while not fim_arquivo:
    linha = arquivo.readline()
    if linha =='':
        fim_arquivo = True
    else:
        linha = linha.rstrip()
        times.append(linha)
arquivo.close()
times.sort()

print('-', times)
