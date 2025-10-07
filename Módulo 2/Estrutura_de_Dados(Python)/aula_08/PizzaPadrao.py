# Classe pai - SuperClass()
class PizzaPadrao:
    def __init__(self, sabor, tamanho, preco, ingredientes):
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco = preco
        self.ingredientes = ingredientes

    def mostrar_detalhes (self):
        print(f'''
        --- 🍕Detalhes da Pizza ---
                Sabor: {self.sabor}
                Tamanho: {self.tamanho}
                Preço: R$ {self.preco}
                Ingredientes: {self.ingredientes}
            ''')