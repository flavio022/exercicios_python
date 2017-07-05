try:
 arquivo_entrada = open('jogos_turno_unico.txt', 'r')
 arquivo_saida = open('resultados_jogos_turno_unico.txt', 'w')
 for linha in arquivo_entrada:
     info = linha.rstrip().split(':')
     timeA = info[0]
     timeB = info[1]
     print('\nJogo:', timeA, 'x', timeB)
     golsA = int(input('Número de gols marcados pelo ' + timeA + ': '))
     golsB = int(input('Número de gols marcados pelo ' + timeB + ': '))
     arquivo_saida.write(timeA + ':' + str(golsA) + ':' + timeB + ':' +
str(golsB) + '\n')
     arquivo_entrada.close()
     arquivo_saida.close()
except FileNotFoundError:
     print('Arquivo jogos_turno_unico.txt não encontrado!')
