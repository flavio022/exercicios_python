estoque ={"smart tv 40" : [2500.00, 12],
          "smart tv 50" : [3250.00, 7 ],
          "home teather" : [3250.00, 10 ],
          "notebook i3" : [2900.00, 6 ],
          "notebook i7" : [3400.00, 4]}
venda = [["home teather",3],["notebook i3",2],["smart tv 50",5],["notebook i7",5]]

for preco in estoque:
    estoque[preco][0] = estoque[preco][0]*1.05
total = 0
for opercao in venda:
    produto,quantidade = opercao
    preco = estoque[produto][0]
    custo = quantidade * preco
    if estoque[produto][1]>quantidade:
        print(produto, "\t\t", quantidade, "\t\t", format(preco,'.2f'),"\t\t", format(custo,'.2f'))
        estoque[produto][1] -= quantidade
        total +=custo
       
print("\nCusto total:", format(total, '.2f'))

print("Estoque")
for chave, dados in estoque.items():
    
    print("Descriçao: ", chave)
    print("Preço: ", dados[0])
    print("Quantidade: ",dados[1])
          
          
