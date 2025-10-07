# #Nessa aula aprenderemos sobre vetores, listas.

# #definido o vetor
# quantidade = 500
# notas = [0.0]*5
# soma = 0.0
# #varrendo o vetor
# for i in range(5):
#     notas[i] = float(input("Informe uma nota: "))
#     soma = soma + notas[i]

# print(f'vetor de notas: {notas}, com soma {soma}')
# media = soma/quantidade
# print(f'vetor de nota: {notas}, com soma {soma} e media {media}')

# for i in range (5):
#     if notas[i] >= media:
#         print (f'Aluno {i} com notas {notas[i]} Aprovado')
#     else:
#         print(f'Aluno {i} com notas {notas[i]} Reprovado')

# #ATIVIDADE: Escreva um programa que armazene 10 números inteiros em um vetor e exiba o maior e o menor valor armazenado.
# numeros = [12,18,13,41,15,99,200]
# maior = numeros[0]
# menor = numeros[0]

# for i in range(len(numeros)):
#     if numeros[i] > maior:
#         maior = numeros[i]
#     if numeros[i] < menor:
#         menor = numeros[i]
# print(f'O maior numero é {maior}')
# print(f'O menor numero é {menor}')

#Mais exercicios ATIVIDADE:
#Ex1: Faça um programa que lê 10 números inteiros e imprima os valores em ordem reversa.

# Cria uma lista vazia para armazenar os números
# numeros = []

# # Pede ao usuário para inserir 10 números
# for i in range(10):
#   numero = int(input(f"Digite o número {i + 1}: "))
#   numeros.append(numero)

# # Imprime os números em ordem reversa
# numeros.reverse()
# print("Números em ordem reversa:", numeros)

#Ex2: Faça um programa que lê 10 números inteiros e produza um vetor onde cada elemento é o quadrado do vetor original. Imprimir o resultado
# vetor_original = []
# for i in range(10):
#   numero = int(input(f"Digite o número {i + 1}: "))
#   vetor_original.append(numero)

# vetor_quadrado = []
# for numero in vetor_original:
#   vetor_quadrado.append(numero**2)
# print("Elementos do vetor:", vetor_original)
# print("Elementos do vetor ao quadrado:", vetor_quadrado)

#Ex3: Faça um programa que lê 10 números inteiros e os armazena em um vetor, e calcula e mostra dois vetores resultantes:
# a) O primeiro vetor resultante deve conter os números positivos;
# b) O segundo deve conter os números negativos. 
# Cada vetor resultante vai ter, no máximo, 10 posições, que podem não ser completamente utilizadas, sendo que as posições vazias devem ficar ao final do vetor. 

# vetor_original = []
# vetor_positivo = []
# vetor_negativo = []
# for i in range(10):
#     numero = int(input(f"Digite o número {i + 1}: "))
#     vetor_original.append(numero)
#     if numero > 0:
#         vetor_positivo.append(numero)
#     elif numero < 0:
#         vetor_negativo.append(numero)

# print(f"Elementos: {vetor_original}")
# print(f"Elementos Positivos: {vetor_positivo}")
# print(f"Elementos Negativos: {vetor_negativo}")

#Ex4: Criar 3 vetores com 10 posições, o primeiro contendo o nome do aluno, um segundo com a cidade ('Rio de janeiro', 'Niteroi', 'Petropolis', 'Teresopolis') e  um terceiro com a idade.
# a) Imprimir os alunos por cidade
# b) Imprimir a media de idade por cidade

print('***Cadastro de alunos***')

quantidade = 10
nome_aluno = [0] * quantidade
cidade_aluno = [0] * quantidade
idade_aluno = [0] * quantidade

# Varrer o vetor
for i in range(quantidade):
    nome_aluno[i] = (input(f'Informe o nome do aluno {i+1}/{quantidade}: '))
    cidade_aluno[i] = (input(f'Informe a cidade do aluno {i+1}/{quantidade} (Escolha entre: Rio de Janeiro, Niterói, Petrópolis e Teresópolis): '))
    idade_aluno[i] = int(input(f'Informe a idade do aluno {i+1}/{quantidade}: '))
    

print(f'Vetor de nome dos alunos é: {nome_aluno}.')
print(f'Vetor de cidade dos alunos é: {cidade_aluno}.')
print(f'Vetor de idade dos alunos é: {idade_aluno}.')


# a) Imprimir os alunos por cidade
print('\n***ALUNOS POR CIDADE***\n')

cidades = ['Rio de Janeiro', 'Niterói', 'Petrópolis', 'Teresópolis']

for cidade in cidades:
    print(f'\nCidade de/do {cidade}:')
    for i in range(quantidade):
        if cidade_aluno[i] == cidade:
            print(nome_aluno[i])
        else:
            print(f'Não há alunos cadastrados nesta cidade.')

# b) Imprimir a media de idade por cidade
        
for cidade in cidades:
    soma_idade = 0
    contador_cidade = 0  # Contador de alunos na cidade atual

    for i in range(quantidade):
        if cidade_aluno[i] == cidade:
            soma_idade += idade_aluno[i]
            contador_cidade += 1

    if contador_cidade > 0:
        media_idade = soma_idade / contador_cidade #calculo da média de idades
        print(f'Média de idade de/do {cidade}: {media_idade:.2f}')
    else:
        print(f'Não há alunos cadastrados em/no {cidade}.')

#CODIGO INCOMPLETO!!!!!!!!!!! É PRECISO --> Imprimir os alunos por cidade e Imprimir a media de idade por cidade



