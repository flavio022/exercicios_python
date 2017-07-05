"""Desenvolva um programa que leia os times cadastrados no arquivo "arquivos.txt"
e ultilize estes times para montar um campeonato do tipo todos contra todos
em turno único, onde cada um dos competidores enfrenta todos os demais apenas uma vez
Por exemplo, se tivermos somente 3 times  cadastrados no arquivo, o seu programa
devera apresentar como resultado a seguinte lista de jogos:
*Guarani x portugues
*guarani x palmeiras
*portuguesax palmeiras"""
fim_arquivo = False
arquivo = open('arquivos.txt', 'r')
times = []
while not fim_arquivo:
    linha = arquivo.readline()
    if linha == '' :
        fim_arquivo = True
    else:
        linha = linha.rstrip()
        times.append(linha)
arquivo.close()
for t1 in range(len(times)):
    for t2 in range(t1-1,len(times)):
        print(times[t1],'x',times[t2])
        
