#Pegue a lista do exercício 2 e quebre em 2 listas: a 1ª com os elementos 0 a (tamanho/2-1) 
# e a 2ª de (tamanho/2) a (tamanho). Apresente as listas 
import random

lista = [random.randint(1, 100) for _ in range(15)]
print("Lista Original: ", lista)
#Caluculando o meio da lista:
meio = len(lista)//2 #Divisão inteira

#Dividindo a lista em 2 partes
lista_1 = lista [:meio]
lista_2 = lista [meio:]

print("Primeira metade da lista: ", lista_1)
print("Primeira metade da lista: ", lista_2)

