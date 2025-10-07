def fazer_pedido(cardapio):
    pedido = []
    
    while True:
        sabor = input("Digite o sabor da pizza que deseja (ou 'sair') para finalizar.")
        if sabor == "sair":
            break
        elif sabor in cardapio:
            pedido.append(sabor)
            print(f'{sabor} adicionado no seu pedido!')
        else:
            print(f'Esse sabor não está disponível. Escolha outro sabor.')
    return pedido

cardapio = ["Mussarela", "Calabresa", "Pepperoni"]
pedido_cliente = fazer_pedido(cardapio)
print(pedido_cliente)