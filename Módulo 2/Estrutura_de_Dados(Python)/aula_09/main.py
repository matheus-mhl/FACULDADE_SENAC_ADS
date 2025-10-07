#Neste arquivo estarão presentes todos os comandos utilizados para fazer com que o sisma funcione
from PizzaPadrao import PizzaPadrao
from PizzaDoce import PizzaDoce
# Criando objetos
pizza_comum = PizzaPadrao("Calabresa", "Família", 29.99, "Tomate e cebola")
pizza_chocolate = PizzaDoce("Chocolte com Morango", "Pequena", 39.99, "Chocoate & Morango", "Chocolate")
        
print("--- Pizza Comum---")
pizza_comum.mostrar_detalhes()
print("--- Pizza Doce---")
pizza_chocolate.mostrar_detalhes()