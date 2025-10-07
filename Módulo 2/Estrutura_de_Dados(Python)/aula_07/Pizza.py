class Pizza:
    # Atributos da Classe (Construtor padrão)
    def __init__(self, sabor, tamanho, preco):
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco = preco

    #Método nosso criado para descrever
    # ("Calabresa", "Pequeno", 29.90) - Organização do codigo abaixo
    def descricao(self):
        return f"Pizza de {self.sabor}, Tamanho: {self.tamanho}, Preço: R${self.preco:.2f}"
    
# Criando objetos da classe Pizza
pizza1 = Pizza("Calabresa", "Família", 52.00)
pizza2 = Pizza("Mussarel", "Média", 49.90)
pizza3 = Pizza("Portuguesa", "Pequena", 29.90)
print(pizza1.descricao())
print(pizza2.descricao())
print(pizza3.descricao())