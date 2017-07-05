produto = {}
while True:
    nome = input("Digite o nome do produto: ")
    if nome in produto:
        print("Produto já cadastrado: ")
    elif nome == "sair":
        break
    else:
        preco = float(input("Digite o preço do produto!!"))
        produto[nome] = preco
while True:
    print("""-------MENU DE OPÇÕES-------
(1)Consultar preco de um produto
(2)Apagar produto
(3)Alterar preço do produto
(4)Sair
""")
    op = int(input("Escolha uma opção: "))
    if op == 1:
        nome = input("Digite o nome do produto: ")
        if nome in produto:
            preco = produto[nome]
            print("Preço R$",format(preco,'.2f'))
        else:
            cad = input("Produto não cadastrado, deseja cadastrar? [s/n]")
            if cad == 's':
                nome = input("Nome do produto: ")
                preco = float(input("Preço do produto: "))
                estoque[nome] = preco
    if op == 2:
        nome = input("Digite o nome do produto: ")
        if nome in produto:
            preco = produto[nome]
            print("Preço R$",format(preco,'.2f'))
        
            
    
        
    
        

