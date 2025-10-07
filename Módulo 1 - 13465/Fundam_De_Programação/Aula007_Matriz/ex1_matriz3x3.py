# 1 - Faça um programa que preencha uma matriz 3x3 com números inteiros e multiplique todos os seus valores por 2. Apresente ambas matrizes.

# Criamos uma lista vazia chamada 'matriz' que vai armazenar as 3 linhas da nossa matriz 3x3.
matriz = []

# Informamos ao usuário o que ele precisa fazer.
print("Digite os valores da matriz 3x3:")

# Usamos dois laços for aninhados para preencher a matriz.
# O primeiro 'for' representa as linhas.
for i in range(3):
    linha = []  # Criamos uma nova lista para armazenar os elementos da linha atual.

    # O segundo 'for' representa as colunas da matriz.
    for j in range(3):
        # Solicitamos que o usuário digite um número para a posição [i][j] da matriz.
        valor = int(input(f"Elemento [{i}][{j}]: "))

        # Adicionamos o valor digitado à lista 'linha'.
        linha.append(valor)

    # Após preencher a linha com 3 elementos, adicionamos ela à matriz principal.
    matriz.append(linha)

# Agora vamos criar uma nova matriz que conterá os valores da matriz original multiplicados por 2.
matriz_dobrada = []

# Novamente, usamos dois laços for para percorrer a matriz original.
for i in range(3):
    linha = []  # Lista temporária para a nova linha da matriz dobrada.

    for j in range(3):
        # Multiplicamos o valor da matriz original por 2.
        valor_dobrado = matriz[i][j] * 2

        # Adicionamos o valor dobrado à nova linha.
        linha.append(valor_dobrado)

    # Adicionamos a nova linha completa à matriz dobrada.
    matriz_dobrada.append(linha)

# Agora vamos exibir as duas matrizes para o usuário.

print("\nMatriz original:")
for linha in matriz:
    print(linha)  # Cada linha é uma sublista da matriz original.

print("\nMatriz multiplicada por 2:")
for linha in matriz_dobrada:
    print(linha)  # Cada linha é uma sublista da nova matriz com os valores dobrados.

