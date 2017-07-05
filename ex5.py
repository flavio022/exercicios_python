
lista = []

print("Escolha uma opção: ")
print("(1) Cadastrar um amigo")
print("(2) Mostrar nomes de todos os amigos")
print("(9) Sair do programa")
op = int(input())

if op == 1:
    nome = input("Digite o nome do amigo")
    lista.append(nome)
elif op == 2:
    print(lista)
elif op == 9:
    print("Fim !")

   
    

    

