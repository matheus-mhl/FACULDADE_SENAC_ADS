#Faça um Programa que peça  idade e  altura de 5 pessoas, armazene cada informação em listas
# diferentes. Imprima a idade e altura na ordem inversa da ordem lida.
idade = []
altura = []

for i in range (3):
    idade_num = int(input("Digite sua idade: "))
    idade.append(idade_num)
    altura_num = float(input("Digite sua altura: "))
    altura.append(altura_num)


idade.reverse()
altura.reverse()

print("\nIdades na ordem inversa:", idade)
print("Alturas na ordem inversa:", altura)
