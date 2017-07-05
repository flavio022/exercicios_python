arquivo = open("produtos.txt",'r')

total =[]
for linha in arquivo:
    produtos = linha.rstrip().split(':')
    quantidade = produtos[0]
    valor = produtos[1]  
    produto = produtos[2]
    subtotal = int(valor) * int(quantidade)
    print("Produto: ",produto,"-","Subtotal R$:", subtotal)
    total.append(subtotal)
for i in total:
    print(i)
    

    
