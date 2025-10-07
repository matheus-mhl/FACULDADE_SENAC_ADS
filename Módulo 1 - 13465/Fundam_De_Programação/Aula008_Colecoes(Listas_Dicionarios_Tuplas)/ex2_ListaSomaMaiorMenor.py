#Faça um Programa que crie uma lista de 15 números inteiros aleatórios, mostre a lista original, a soma dos elementos, o maior, o menor e o produto dos elementos (dica: use funções max() e min() )
import random
import math

#Caso queira escolher os números da lista manualmente utilize o código abaixo:
# lista = []
# for i in range (15):
#     num = int(input(f"Digite o {i+1}° número inteiro: "))
#     lista.append(num)

# Caso o contrário utilize o seguinte código para criar lista com 15 números inteiros aleatórios entre 1 e 100 AUTOMATICAMENTE
lista = [random.randint(1, 100) for _ in range(15)]

    
# Exibir a lista original
print("Lista original:", lista)

# Calcular a soma dos elementos
soma = sum(lista)
print("Soma dos elementos:", soma)

# Encontrar o maior e o menor valor
maior = max(lista)
menor = min(lista)
print("Maior valor:", maior)
print("Menor valor:", menor)

# Calcular o produto dos elementos
produto = math.prod(lista)
print("Produto dos elementos:", produto)

    