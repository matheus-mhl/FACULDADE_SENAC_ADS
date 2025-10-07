#Faça um Programa que leia 20 números inteiros e armazene-os em 3 listas: todos, pares e impares. Imprima as três listas.
todos = []
pares = []
impares = []

for i in range ():
    num = int(input(f"Digite o {i+1}° número inteiro: "))
    todos.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Todos:", todos)
print("Pares:", pares)
print("Ímpares:", impares)
    