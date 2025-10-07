# ---------------------------------------------------------
# 📘 Exercício SENAC — Tuplas: Cadastro de Produtos com Preço Fixo
# ---------------------------------------------------------

# Contexto:
# Você está desenvolvendo um sistema simples para registrar produtos em uma loja.
# Cada produto terá nome e preço fixo, e esses dados não devem ser alterados após o cadastro.
#
# Como os dados serão imutáveis, use tuplas para armazenar cada produto.

# ---------------------------------------------------------
# 📝 Enunciado:
# ---------------------------------------------------------
# Crie um programa Python que permita ao usuário:
# - Cadastrar produtos (nome + preço) como tuplas.
# - Visualizar todos os produtos cadastrados.
# - Sair do programa.

# ---------------------------------------------------------
# 🔧 Requisitos:
# ---------------------------------------------------------
# - Cada produto deve ser armazenado como uma tupla com dois elementos: (nome, preco).
# - Os produtos devem ser armazenados em uma lista de tuplas.
# - O programa deve exibir um menu de opções com as 3 ações mencionadas.
# - Ao visualizar os produtos, exiba o nome e o preço com duas casas decimais.

# 💡 Exemplo de estrutura interna dos dados:
# produtos = [
#     ("Mouse", 89.90),
#     ("Teclado", 149.50),
#     ("Monitor", 799.00)
# ]

# 🎯 Exemplo de saída esperada (uso do programa):
# === Cadastro de Produtos ===
# 1. Cadastrar novo produto
# 2. Visualizar produtos cadastrados
# 3. Sair
# Escolha uma opção: 1
# Digite o nome do produto: Teclado
# Digite o preço do produto: 149.5
# Produto cadastrado com sucesso!
#
# === Cadastro de Produtos ===
# 1. Cadastrar novo produto
# 2. Visualizar produtos cadastrados
# 3. Sair
# Escolha uma opção: 2
#
# Produtos cadastrados:
# 1. Teclado - R$ 149.50

# ---------------------------------------------------------
# ✅ Resolução do exercício:
# ---------------------------------------------------------

# Criamos uma lista vazia chamada 'produtos' que armazenará tuplas (nome, preço)
produtos = []

# Início do laço principal do programa, que mantém o menu ativo até que o usuário escolha sair
while True:
    # Exibe o menu de opções
    print("\n=== Cadastro de Produtos ===")
    print("1. Cadastrar novo produto")
    print("2. Visualizar produtos cadastrados")
    print("3. Sair")

    # Recebe a opção escolhida pelo usuário
    opcao = input("Escolha uma opção: ")

    # ---------------------------------------------------------
    # Opção 1 - Cadastrar novo produto
    # ---------------------------------------------------------
    if opcao == "1":
        # Solicita o nome do produto
        nome = input("Digite o nome do produto: ")
        try:
            # Solicita o preço do produto e tenta converter para float
            preco = float(input("Digite o preço do produto: "))
        except ValueError:
            # Caso o usuário digite algo inválido (ex: letras), exibe erro
            print("Preço inválido. Digite um número com ponto.")
            continue  # Retorna ao menu principal

        # Cria a tupla com os dados do produto
        produto = (nome, preco)

        # Adiciona a tupla à lista de produtos
        produtos.append(produto)

        # Mensagem de sucesso
        print("Produto cadastrado com sucesso!")

    # ---------------------------------------------------------
    # Opção 2 - Visualizar todos os produtos cadastrados
    # ---------------------------------------------------------
    elif opcao == "2":
        # Verifica se a lista está vazia
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            # Exibe os produtos formatados
            print("\nProdutos cadastrados:")
            for i in range(len(produtos)):
                nome, preco = produtos[i]  # Desempacota a tupla
                print(f"{i + 1}. {nome} - R$ {preco:.2f}")  # Exibe com duas casas decimais

    # ---------------------------------------------------------
    # Opção 3 - Sair do programa
    # ---------------------------------------------------------
    elif opcao == "3":
        print("Encerrando o programa. Até logo!")
        break  # Interrompe o laço e encerra o programa

    # ---------------------------------------------------------
    # Opção inválida
    # ---------------------------------------------------------
    else:
        print("Opção inválida. Tente novamente.")
