agenda ={}
while True:
    nome = input("Digite um nome ou 'sair' para encerrar")
    if nome == "sair":
        break
    else:
        tel = int(input("Digite um telefone"))
        agenda[nome] = tel
while True:
    print("""MENU DE OPÇÕES:
(1)INSERIR UM TELEFONE
(2)CONSULTAR TELEFONE
(3)EXCLUIR UM TELEFONE
""")
    op = int(input("Escolha uma opção"))
    if op == 1:
        nome = input("Digite o nome para inserir")
        if nome in agenda:
            print("Usuario já cadastrado")
            print(agenda[nome].items)
            alterar = input("Deseja alterar o numero?")
            if alterar == "sim":
                tel = int (input("Digite novo numero"))
                agenda[nome] = tel
        else:
            tel = int(input("Digite telefone"))
    elif op == 2:
        nome = input("Digite o nome para consulta")
        if nome in agenda:
            print(agenda[nome])
        else:
            alterar = input("Usuario não cadastrado, deseja cadastrar?")
            if alterar == "sim":
                nome = input("Digite o nome ")
                tel = int(input("Digite o telefone "))
                agenda[nome] = tel
                print("Usuario Cadastrado com sucesso")
    elif op == 3:
        break;
