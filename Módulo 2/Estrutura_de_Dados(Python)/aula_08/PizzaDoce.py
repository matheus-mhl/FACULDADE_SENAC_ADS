#Classe Filha - subclass()
from PizzaPadrao import PizzaPadrao
class PizzaDoce(PizzaPadrao):
    def __init__(self, sabor, tamanho, preco, ingredientes, borda_recheada):
        super().__init__(sabor, tamanho, preco, ingredientes) 
        # """super""" -- >Utilizado para chamar a "classe pai"
        # """__init__()""" é o construtor da classe
        self.borda_recheada = borda_recheada
        
    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f'''
              Borda recheada: {self.borda_recheada}
              ''')
        
# Criando objetos
pizza_comum = PizzaPadrao("Calabresa", "Família", 29.99, "Tomate e cebola")
pizza_chocolate = PizzaDoce("Chocolte com Morango", "Pequena", 39.99, "Chocoate & Morango", "Chocolate")
        
print("--- Pizza Comum---")
pizza_comum.mostrar_detalhes()
print("--- Pizza Doce---")
pizza_chocolate.mostrar_detalhes()