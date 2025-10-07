# Questão 3: Dicionários e Estruturas Condicionais

# Gere um programa contendo um dicionário “estoque_loja”, onde cada produto 
# é uma chave e o valor é seu preço" (float) 
# Exemplo: estoque_loja = {"Camiseta": 29.90, “Calça: 101.00... }. 
# Adicione pelo menos três produtos.

# Implemente uma função adicionar_produto(nome_produto, preco) que:
# •	adiciona um produto caso ele não exista;
# •	Exiba mensagem “Produto já existe” caso ele exista;

# Implemente uma função lista_produtos() que:
# •	Lista os produtos em estoque_loja;
# •	Exiba mensagem “lista vazia” caso não exista produto;

# Implemente uma função remove_produtos(nome_produto) que:
# •	Remove o produto de estoque_loja;
# •	Exiba mensagem “Produto não existe” caso ele não exista;

# No código principal, faça um loop que:
# •	Mostre um menu com as ações: "listar", "adicionar", "remover" ou "sair". 
# •	De acordo com a escolha, leia dados e chame a respectiva função 

#RESPOSTA
#Gere um programa contendo um dicionário “estoque_loja”, onde cada produto é uma chave e o valor é seu preço" (float) Exemplo: estoque_loja = {"Camiseta": 29.90, “Calça: 101.00... }. Adicione pelo menos três produtos.
estoque_loja = {
    "Camiseta": 29.90,
    "Calça": 101.00,
    "Tênis": 199.90
}

# Adicionando produtos
def adicionar_produto(nome_produto, preco):
    if nome_produto in estoque_loja:
        print("Produto já existe.")
    else:
        estoque_loja[nome_produto] = preco
        print(f"Produto '{nome_produto}' adicionado com sucesso!")

# Listando e Removendo produtos
def lista_produtos():
    if not estoque_loja:
        print("Lista vazia.")
    else:
        print("Produtos em estoque:")
        for produto, preco in estoque_loja.items():
            print(f"- {produto}: R$ {preco:.2f}")

def remove_produto(nome_produto):
    if nome_produto in estoque_loja:
        del estoque_loja[nome_produto]
        print(f"Produto '{nome_produto}' removido com sucesso.")
    else:
        print("Produto não existe.")




# Criando Menu
def menu():
     while True:
         print("\nMenu:")
         print("1 - Listar produtos")
         print("2 - Adicionar produto")
         print("3 - Remover produto")
         print("4 - Sair")

         opcao = input("Escolha uma opção: ").strip() #método de strings que remove caracteres específicos do início e do fim de uma string

         if opcao == "1":
             lista_produtos()
         elif opcao == "2":
             nome = input("Digite o nome do produto: ").strip()
             try:
                 preco = float(input("Digite o preço do produto: ").strip())
                 adicionar_produto(nome, preco)
             except ValueError:
                 print("Preço inválido. Digite um número.")
         elif opcao == "3":
             nome = input("Digite o nome do produto a remover: ").strip()
             remove_produto(nome)
         elif opcao == "4":
             print("Saindo do programa.")
             break
         else:
             print("Opção inválida. Tente novamente.")

#Utilizando função menu
menu()

