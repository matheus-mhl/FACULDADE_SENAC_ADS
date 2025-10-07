#Pegue a lista do exercício 2 e verifique se o numero 10 faz parte da lista gerada
# (dica: utilize a construção “if x in <lista>”)
import random
lista = [random.randint(1, 100) for _ in range(15)]
num10 = 10
print(lista)
if num10 in lista:
    print("O número 10 faz parte da lista.")
else:
    print("O numero 10 não faz parte da lista")


