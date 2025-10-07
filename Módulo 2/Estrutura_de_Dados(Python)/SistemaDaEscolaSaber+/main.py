from Pessoa import Pessoa, Professor, Aluno, Funcionario #importando dados do arquivo "Pessoa.py"

#Tentando ORGANIZAR estrutura:

# Traceback (most recent call last):
#   File "c:\Users\36134652025.1M\Desktop\FACULDADE SENAC (ADS)\Módulo 2\Estrutura_de_Dados(Python)\SistemaDaEscolaSaber+\main.py", line 4, in <module>
#     professor1 = Professor("Carlos", 40,"Matemática")
#                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "c:\Users\36134652025.1M\Desktop\FACULDADE SENAC (ADS)\Módulo 2\Estrutura_de_Dados(Python)\SistemaDaEscolaSaber+\Pessoa.py", line 24, in __init__
#     super().__init__(nome, idade, disciplina)
# TypeError: Pessoa.__init__() missing 2 required positional arguments: 'endereco' and 'telefone' 
#Criando objetos

professor1 = Professor("Carlos", 40,"Matemática")
aluno1 = Aluno("Maria", 16, "2025A01")
funcionario1 = Funcionario("João", 36, "Bibliotecário")

#Saída:
print("--- Professor ---")
professor1.mostrar_detalhes()
print("--- Aluno ---")
aluno1.mostrar_detalhes
print("--- Funcionário ---")
funcionario1.mostrar_detalhes





# ...
# Disciplina: Matemática

# --- Aluno ---
# Nome: Maria, Idade: 16
# ...
# Matrícula: 2025A01

# --- Funcionário ---
# Nome: João, Idade: 35
# ...
# Cargo: Bibliotecário