# 2 - Faça um programa que leia valores inteiros em duas matrizes 3x3 imprima ambas matrizes e a matriz soma das duas.
mat1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
mat2 = [
    [1,1,1],
    [2,2,2],
    [3,3,3]
]

mat_soma = []

# Matriz que vai armazenar o resultado da soma
mat_soma = []

# Percorre as linhas (i)
for i in range(3):
    linha = []
    # Percorre as colunas (j)
    for j in range(3):
        # Soma os elementos das duas matrizes na posição [i][j]
        valor = mat1[i][j] + mat2[i][j]
        linha.append(valor)
    # Adiciona a linha somada à matriz final
    mat_soma.append(linha)

# Exibe a matriz resultante
print("Matriz Soma:")
for linha in mat_soma:
    print(linha)
