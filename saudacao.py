fim_arquivo = False
arquivo = open('times.txt','r')
times = []
while not fim_arquivo:
    linha = arquivo.readline()
    if linha == '':
        fim_arquivo = True
    else:
        linha = linha.rstrip()
        times.append(linha)
for t1 in range(len(times)):
    for t2 in range(t1+1,len(times)):
        print(times[t1],'x',times[t2])
