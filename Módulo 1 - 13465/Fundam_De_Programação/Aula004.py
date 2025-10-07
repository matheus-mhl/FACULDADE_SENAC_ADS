#Estrutura de Repetição com Python: "FOR" e "WHILE"
#Exemplo 1 
# for i in range (1,51): #esse código fará a máquina contar do numero 1 até 50
#     print(i)

#Exemplo 2
# frutas = ['maça', 'banan', 'pera', 'abacate', 'uva']
# for x in frutas:
#     print(x)

#Exemplo 3
# for cont in range(1,31):
#     print (f"/n***Aluno {cont}***")
#     n1 = float(input("Informe a primeira nota:"))
#     n2 = float(input("Informe a segunda nota:"))
#     media = (n1 + n2)/2
#     print(f'Aluno{cont} - Media das notas {n1} e {n2} = {media}')

# print("Fim do programa!!")

#Exemplo 4 - Faça um programa que leia 10 valores inteiros, um de cada vez, e encontre quantos destes valores são pares, quantos são ímpares, além de calcular a média de todos os números informados. Todos os dados calculados devem ser exibidos ao final do programa. 
# num=int(input("Entre com um numero inteiro: "))
# if (num%2==0):
#     print(f"numero {num} é par")
# else:
#     print(f"de {num} é impar ")

#Exemplo 5 - Faça um programa que leia as notas (n1 e n2) de 10 alunos e 
# 1 --> Calcule e imprima e média
# 2 --> Diga se foi aprovado (media >= 7) ou reprovado (media <7)

# for nota in range(1,11):
# print("A nota do Aluno foi de:")
# n1 = float(input("Insira o valor da primeira nota: "))
# n2 = float(input("insira o valor da segunda nota: "))
# nota = (n1 + n2)/2
# print (f"A nota final do aluno foi de: {nota})")
# if nota>7:
#     print ("O aluno foi aprovado!!")
# else: print ("O aluno foi reprovado :( ")
    
#Agora é com vocês...
#Exercicio 1 - Faça um programa que imprima a tabuada de 10 utilizando estrutura de repetição. 

# for n in range(1,11):
#     print(f'{n} x 10 = {n*10}')

#Exercicio 2 - Faça um programa que imprima a tabuada de um numero “n” (dado de entrada do seu programa)  utilizando estrutura de repetição.
# n = int(input("Escolha um número: "))
# for t in range(1,11):
#     print (f'{n} x {t} = {n * t}')
    
#Exercicio 3 - Escreva um programa que lê 10 valores inteiros para a variável “a”, um de cada vez, e conta quantos destes valores são negativos, exibindo esta informação na tela. 

#TENTATIVA de resolver exercicio com codigo dos exerciccios anteriores, utilizando a tabuada.
# a = int(input("Digite qualquer número inteiro, positivo ou negativo: "))
# for programa in range (1,11):
#     print (f'{a} x {programa} = {a*programa}')
# if a*programa >=0:
#     print ("O valor é positivo")
# else:
#     print ("O valor é negativo")

#CORREÇÃO do exercicio 3
# ContadorPositivo = 0
# ContadorNegativo = 0

# for i in range(1, 11):
#     numero = int(input("Digite um número: "))
#     if numero >= 0:
#         ContadorPositivo += 1
#     else:
#         ContadorNegativo += 1

# print("Quantidade de números positivos:", ContadorPositivo)
# print("Quantidade de números negativos:", ContadorNegativo)


    

