#Desafio Prático 1: Sistema de Pedido Online

# **Objetivo:** Criar um sistema completo de pedido de pizzas usando listas, dicionários e estruturas de repetição.

# Instruções:

# Você foi contratado para aprimorar o sistema de pedidos da Pizzaria Sabores. O seu desafio é construir um programa que:

# 1. **Exiba um cardápio:** Crie um **dicionário** para armazenar o cardápio da pizzaria, contendo pelo menos 5 sabores e seus respectivos preços (por exemplo, `{"Mussarela": 30.00, "Calabresa": 32.00}`).
# 2. **Receba o pedido:** Use um **loop `while`** para permitir que o cliente adicione vários sabores ao pedido. O loop deve continuar até que o cliente digite "sair". Armazene os sabores escolhidos em uma **lista**.
# 3. **Calcule o total:** Percorra a lista de pedidos com um **loop `for`** e calcule o valor total a ser pago, somando os preços de cada pizza com base no dicionário do cardápio.
# 4. **Imprima o resumo:** Ao final do pedido, imprima um resumo formatado, mostrando cada pizza pedida e o valor total final.


#1. Solução para PRIMEIRA parte do exercício:
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
#FIM da solução do tópico 1.

#2. Solução para a SEGUNDA parte do exercício:
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

#3. Solução para a TERCEIRA parte do exercício:
total = 0
for sabor in pedido:
    total += cardapio[sabor]
#FIM da solução do tópico 3.

#4. Solução para a TERCEIRA parte do exercício.
print("========== RESUMO DO PEDIDO ==========")
if pedido: #Verifica se existe algum valor em pedido
    for sabor in pedido:
        print(f"--> {sabor}: R${cardapio[sabor]:.2f}") #Devolve o valor do sabor da pizza se ela estive no docionario cardapio.
    print(f"Total a pagar: R${total:.2f}")
else:
    print("Nenhuma pizza foi pedida. Volte sempre.")