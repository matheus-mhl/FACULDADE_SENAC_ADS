#Aprendendo a utilizar o comenado WHILE

#Exemplo 1 - Imprimir os números de 1 a 10.
# numero = 1
# while (numero <= 10):
#     print (numero)
#     numero = numero +1

#Exemplo 2 - Faça um programa que exiba na tela os números ímpares entre 100 e 200. O programa deve fazer uso da estrutura de repetição while.
# cont=101
# while cont<200:
# 	print(cont)
# 	cont = cont +2
	
#Exemplo 3 - Faça um programa que leia 15 números inteiros, calcule e exiba a média dos números pares.
# i = 1
# soma = 0
# q = 0 #variável q = QUANTIDADE
# while i <=15:      # Le os 15 numeros
#     num = int (input('Informe um número: '))
#     if num % 2 == 0:   # verifica se é par
#         soma = soma + num
#         q+=1
#     i+=1
# if (q > 0):     # Calcula media
#     media = soma / q
#     print(f"Média: {media:.1f}" )
# else:
#     print('Não houve números pares.')

#Utilizando o comando BREAK
#Exemplo 1 - Imprima o valor do divisor.
# a = int( input ("Digite o valor de a: "))
# b = int( input ("Digite o valor de b: "))
# while a < b :   
#     if b % a == 0: # verifica se a divide b      
#         break
#     a += 1
#     print ("O valor do divisor é: ", a )

#Utilizando o comando CONTINUE
#Exemplo 1- Imprima o valor do divisor.
# a = int( input ("Digite o valor de a: "))
# b = int( input ("Digite o valor de b: "))
# while a < b :
#     if b % a == 0: # verifica se a divide b
#         continue
#     a += 1
#     print ("O valor do divisor é: ", a )

#Agora é com vocês
#Exercicio 1 - Faça um programa que mostre na tela os números de  0 até N, onde que N é o limite inserido pelo usuário.
# N = int(input("Digite o número: ")) 
# numero = 0
# while numero <= N:
#     print(numero)
#     numero = numero +1

#Exercício 2 - Faça um programa, utilizando a estrutura while, que permita o usuário fazer contas de adição entre dois valores enquanto ele desejar. (utilize uma estrutura do tipo “Quer continuar S/N ?” para manter o loop)
# 1. Só aceitar os caracteres “S” ou “N”
# 2. Aceitar caracteres “S”, “s”, “N”, “n” (utilize as funções de string)

# while True:
#     n1 = int(input("Digite o primeiro valor: "))
#     n2 = int(input("Digite o segundo valor: "))
#     print(n1 + n2)
#     resp = input("Deseja continuar com a operação? Responda: S ou N --> ")
#     if resp == 's' or resp == 'S':
#         continue
#     if resp == 'n' or 'N':
#         break
# print("Operação Finalizada.")

#Exercicio 3 - Faça um programa que leia um caractere e enquanto não se digitar “F” o programa escreve “dentro do loop”. Ao final escrever “fim do programa”.
# Read = str(input("Digite um caractere: "))
# print(Read)
# resp = input("Digite 'F' para parar o programa: ")
# while resp == 'F':
#     print("fim do programa.")
#     break
# else:
#     print("dentro do loop")



