#Esse arquivo apresenta exercícios sobre a coleção tipo: DICIONARIO
#----------------------------------------------------------------
#Exercicio SENAC:
# Função – Calculadora utilizando funções

# Refaça sua calculadora, agora utilizando funções. Cada operação deve corresponder a uma função, da seguinte forma:

# somar(n1, n2)
# subtrair(n1, n2)
# dividir(n1, n2)
# multiplicar(n1, n2)

# Cada função deverá retornar o resultado da operação, que será apresentado por uma saída(print) geral.

# O menu de opções também deve ser uma função chamada menu(), sem qualquer retorno. 

# Escreva o menu de opções abaixo. 
# Leia a opção do usuário, leia os números e execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida. ​

# ​Escolha a opção:​

# 1- Soma de 2 números inteiros.​

# 2- Diferença entre 2 números (maior pelo menor).​

# 3- Produto entre 2 números.​

# 4- Divisão entre 2 números (o denominador não poderá ser zero).

# 5-. Sair


# Entrada
# Opção de operação e os 2 números

# Saída
# Resultado da operação
#---------------------------------------------------------------------------------------------------------------------------------

#RESPOSTA:

# Funções para operações matemáticas

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    # Retorna a diferença entre o maior e o menor número
    if n1 > n2:
        return n1 - n2
    else:
        return n2 - n1

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    # Verifica se o denominador é zero para evitar erro
    if n2 == 0:
        return None
    else:
        return n1 / n2

def menu():
    print("\n--- Menu de Operações ---")
    print("1 - Soma de 2 números inteiros")
    print("2 - Diferença entre 2 números (maior pelo menor)")
    print("3 - Produto entre 2 números")
    print("4 - Divisão entre 2 números (denominador não pode ser zero)")
    print("5 - Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha a opção: ")

        if opcao == "5":
            print("Encerrando a calculadora. Até logo!")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida. Tente novamente.")
            continue

        try:
            n1 = int(input("Digite o primeiro número inteiro: "))
            n2 = int(input("Digite o segundo número inteiro: "))
        except ValueError:
            print("Entrada inválida. Digite números inteiros.")
            continue

        if opcao == "1":
            resultado = somar(n1, n2)
            print(f"Resultado da soma: {resultado}")

        elif opcao == "2":
            resultado = subtrair(n1, n2)
            print(f"Resultado da diferença (maior - menor): {resultado}")

        elif opcao == "3":
            resultado = multiplicar(n1, n2)
            print(f"Resultado do produto: {resultado}")

        elif opcao == "4":
            resultado = dividir(n1, n2)
            if resultado is None:
                print("Erro: Divisão por zero não é permitida.")
            else:
                print(f"Resultado da divisão: {resultado}")

if __name__ == "__main__":
    main()

