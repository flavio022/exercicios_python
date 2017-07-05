notas = []
for i in range(4):
    notaAlunos = float(input("Digite a nota do aluno %i"%i))
    notas.append(notaAlunos)
media =sum(notas)/4


print(" As notas do alune são:" ,  notas)
print("Sua media é ", media)

