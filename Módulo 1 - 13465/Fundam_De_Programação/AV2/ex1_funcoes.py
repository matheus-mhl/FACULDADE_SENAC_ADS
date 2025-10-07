# Questão 1: Funções e Entrada/Saída de Dados

# Crie um programa contendo uma função apresentar_usuario() que peça ao usuário, 
# seu nome completo e data de nascimento (DD/MM/AAAA), mostrando uma mensagem de boas-vindas,
# e confirmando a data. Crie também a função calcular_idade_aproximada(ano_nascimento), 
# que recebe o ano de nascimento (int) e retorna a idade aproximada,
# considerando o ano atual. No programa principal, chame apresentar_usuario(), 
# extraia o ano da data informada, passe à calcular_idade_aproximada() e exiba a idade do
# usuário.

# Exiba a mensagem, como  ”Roberto nascido em 01/09/2004 tem 21 anos de idade”

#RESPOSTA
def apresentar_usuario(nome, dia, mes, ano):
    return nome, dia, mes, ano
nome=str(input("Informe o seu NOME: "))
dia=str(input("Informe o DIA que você nasceu: "))
mes=str(input("Informe o MÊS que você nasceu: "))
ano=str(input("Informe o ANO que você nasceu: "))
print(f"Bem vindo, {nome} nascido em {dia}/{mes}/{ano}. ")


#Tentando calcular idade
def calcular_idade_aproximada(a, b):
    return a - b
idade = calcular_idade_aproximada (2025, ano)
print(f"Sua idade é de {idade} anos.")

    


    






