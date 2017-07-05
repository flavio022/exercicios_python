try:
    arquivo = open("alunos.txt","r")
    saida = open("medias.txt","w")
    media = []
    for i in arquivo:
        linha = i.rstrip().split(":")
        aluno = linha[0]
        nota1 = linha[1]
        nota2 = linha[2]
        media = float(nota1)+float(nota2)/2
        print(media)
        if media>=6:
            saida.write(aluno+":"+str(media)+"Aprovado"+"\n")
        else:
            saida.write(aluno+":"+str(media)+"Reprovado"+"\n")
    arquivo.close() 
    saida.close()
except FileNotFoundError:
    print("Arquivo não encontrado")
