# Desafio Prático 3: Automatizando Tarefas com Funções

# **Objetivo:** Refatorar o sistema de pedido online usando funções para tornar o código mais modular, organizado e reutilizável.

# Instruções:

# Agora, o desafio é refazer o Desafio Prático 1, mas usando funções para cada parte do processo.

# 1. **Crie uma função `exibir_cardapio()`:** Esta função deve criar o dicionário do cardápio e usar um loop `for` para imprimi-lo na tela.
# 2. **Crie uma função `receber_pedido()`:** Esta função deve conter o loop `while` que recebe os sabores do cliente e os armazena em uma lista. Ela deve **retornar** a lista de pedidos.
# 3. **Crie uma função `calcular_total()`:** Esta função deve receber a lista de pedidos e o dicionário do cardápio como **parâmetros**. Ela deve calcular o valor total e **retornar** o resultado.
# 4. **Execute o fluxo:** No código principal, chame as funções na ordem correta para simular o processo de pedido: `exibir_cardapio()`, `receber_pedido()`, `calcular_total()` e, por fim, imprima o total final.

# 1. **Crie uma função `exibir_cardapio()`:
def exibir_cardapio():
    print("Bem vindo a Pizzaria Sabores, aqui está o nosso cardápio:")
    cardapio = {
        "Mussarela": 30.00,
        "Calabresa": 40.00,
        "Pepperoni": 45.00,
        "Frango": 35.00,
        "Caprese": 60.00
    }

    print("========== CARDÁPIO PIZZARIA SABORES ==========")
    for sabor, preco in cardapio.items():
        print(f"{sabor}: R$ {preco:.2f}")
    return cardapio #Retorna o dicionario "cardapio" para as outras funçoes()
#FIM da solução do tópico 1.

# 2. **Crie uma função `receber_pedido()`:
#A seguir é necessario botar o dicionario "cardapio" entre parenteses da funçao "receber_pedido" para que ela possa 'importar' as informações do dict(dictionary/dicionario)
def receber_pedido(cardapio) :                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    pedido = [] #Lista vazia
    print("Faça seu pedido (digite sair para encerrar):")

    while True:
        sabor_escolhido = input("Escolha um sabor: ")
        if sabor_escolhido.lower() == "sair":
            break #Encerra o loop quando o cliente digita 'sair'
        elif sabor_escolhido in cardapio:
            pedido.append(sabor_escolhido)
            print(f"{sabor_escolhido} adicionado ao seu pedido!!")
        else:
            print("Esse sabor não está no cardápio. Escolha outro.")
#FIM da solução do tópico 2.

# 3. **Crie uma função `calcular_total()`:
    def calcular_total():