arquivo_entrada = open('times_campeonato.txt','r')
arquivo_saida = open('jogos_turno_returno.txt','w')
times = []
for i in arquivo_entrada:
    linha = i.strip().split(':')
    times.append(linha[0])
for i in range(len(times)):
    for j in range(i-1,(len(times))):
        if times[i] == 'Santos':
            arquivo_saida.write(times[i]+":"+times[j]+":"+"Campo do Santos"+"\n")
        elif times[i] == 'Guarani':
            arquivo_saida.write(times[i]+":"+times[j]+":"+"Campo do Guarani"+"\n")
        elif times[i] == 'Vasco':
            arquivo_saida.write(times[i]+":"+times[j]+":"+"Campo do Vasco"+"\n")
        elif times[i] == 'Coritiba':
            arquivo_saida.write(times[i]+":"+times[j]+":"+"Campo do Coritiba"+"\n")
        else:
            arquivo_saida.write(times[i]+":"+times[j]+":"+"Campo do Palmeiras"+"\n")
        
arquivo_entrada.close()
arquivo_saida.close()

