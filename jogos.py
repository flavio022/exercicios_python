fim_arquivo = False
arquivo = open("times_campeonato","r")
times =[]
for linha in arquivo:
    linhas = linha.rstrip()
    times.append(linhas)
arquivo.close()
for t1 in range(len(times)):
    for t2 in range(t1+ 1 , len(times)):
        print(times[t1],'x',times[t2])

