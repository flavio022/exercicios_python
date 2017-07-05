"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene
os resultados em um vetor. Depois, mostre quantas vezes cada valor foi consequido.
"""
import random
lista = []
n = int(input("Digite o número de lançamentos: "))
for i in range(n):
    lista.append(random.randint(1,6))
print(lista)
print()
for i in range(1,7):
    print("A face %i aparece %.2f%% vezes."%(i, 100*lista.count(i)/n))
    
