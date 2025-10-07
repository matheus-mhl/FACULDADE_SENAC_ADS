# Questão 4: Tuplas e Validação de Dados

# Crie uma tupla chamada MESES_DO_ANO contendo os nomes dos 12 meses do ano em português (ex: "Janeiro", "Fevereiro", ...). 

# Em seguida Crie uma função obter_mes_valido(). Esta função deve solicitar ao usuário que "Digite o nome de um mês:". 
# •	Implemente um loop de repetição (while) que continue pedindo a entrada até que o usuário digite um mês que esteja presente na tupla MESES_DO_ANO (considere a entrada case-insensitive, ou seja, "janeiro" ou "Janeiro" devem ser válidos).
# •	Se a entrada for inválida, imprima uma mensagem de erro clara.
# •	A função deve retornar o nome do mês válido (no formato como está na tupla).

# Crie outra função verificar_dias_no_mes(mes).
# •	Esta função deve receber o nome do mês (string).
# •	Usando estruturas condicionais, retorne o número de dias daquele mês (considerando um ano não bissexto para Fevereiro).
# o	Dica: Mês 2: 28 dias. Mês 4, 6, 9, 11: 30 dias. Outros: 31 dias.

# No código principal, chame a função obter_mes_valido() e utilize o mês retornado para chamar verificar_dias_no_mes(). Exiba o resultado final.
# Ex: “Fevereiro tem 28 dias”

#RESPOSTA
meses_do_ano = {
    "JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO",
    "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"
}

def obter_mes_valido():
    while True:
        entrada = input("Digite o nome de um mês: ").upper()

        
        for mes in meses_do_ano:
            if entrada == mes:
                return mes  
        print("Mês digitado de forma incorreta. Tente novamente")

def verificar_dias_no_mes(mes):
    if mes == "Fevereiro":
        return 28
    elif mes in ("Abril", "Junho", "Setembro", "Novembro"):
        return 30
    else:
        return 31


mes_escolhido = obter_mes_valido()
dias = verificar_dias_no_mes(mes_escolhido)
print(f"{mes_escolhido} tem {dias} dias.")


