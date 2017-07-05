#Flávio Tia: 31534112
#EX Lanchonete
pedido = int(input("Quantidade de pedido"))
hotDog =0
bauruS =0
bauruOvo = 0
Hambu = 0
cheese = 0
refrigerante = 0
cont = 0
while cont < pedido:
    codigo = int(input("Codigo pedido"))
    cont += 1
    if codigo == 100:
        hotDog += 1
    elif codigo == 101:
        bauruS += 1     
    elif codigo == 102:
        bauruOvo += 1
    elif codigo == 103:
        Hambu += 1
    elif codigo == 104:
        cheese += 1
    elif codigo == 105:
        refrigerante =+ 1
preco = refrigerante * 4 + Hambu * 8.5 + hotDog * 5 + bauruS * 5.5+ cheese * 10 + bauruOvo * 7
print('A quantidade de pedido é ', cont)
print('O preço a ser pago é R$', preco)




             
