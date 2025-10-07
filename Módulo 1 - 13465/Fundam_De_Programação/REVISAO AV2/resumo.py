#Este arquivo apresenta um RESUMO para a AV2 da matéria de FundamentosDeProgramação:
#Contendo informações sobre: 1. LISTAS, 2. TUPLAS, 3. DICIONARIO & 4. FUNÇÕES

# ======================================================
# 1. LISTAS
# ======================================================
# ✅ O que são?
# Coleções MUTÁVEIS de elementos.
# São definidas usando colchetes []

# 📌 Quando usar?
# Quando os dados podem mudar (tarefas, nomes, valores, etc.)

# 📋 Exemplo:
print("===== LISTAS =====")
frutas = ["maçã", "banana", "laranja"]
print(frutas[1])  # Imprime: banana

frutas.append("uva")       # Adiciona "uva"
frutas.remove("maçã")      # Remove "maçã"
frutas[0] = "abacaxi"      # Altera valor na posição 0

print(frutas)  # Imprime lista atualizada

# ======================================================
# 2. TUPLAS
# ======================================================
# ✅ O que são?
# Coleções IMUTÁVEIS de elementos.
# São definidas com parênteses ()

# 📌 Quando usar?
# Quando os dados NÃO devem mudar (coordenadas, datas, etc.)

# 📋 Exemplo:
print("\n===== TUPLAS =====")
ponto = (10, 20)
print(ponto[0])  # Imprime: 10

# ponto[0] = 15  # ERRO! Tuplas são imutáveis.

# ======================================================
# 3. DICIONÁRIOS
# ======================================================
# ✅ O que são?
# Coleções de pares CHAVE:VALOR, mutáveis.
# Definidos com chaves {}

# 📌 Quando usar?
# Quando quiser associar rótulos a valores (ex: nome → idade)

# 📋 Exemplo:
print("\n===== DICIONÁRIOS =====")
aluno = {
    "nome": "João",
    "idade": 20,
    "curso": "ADS"
}

print(aluno["nome"])  # Imprime: João

aluno["idade"] = 21     # Atualiza idade
aluno["nota"] = 9.5     # Adiciona nova chave

print(aluno)

# ======================================================
# 4. FUNÇÕES ("def")
# ======================================================
# ✅ O que são?
# Blocos reutilizáveis de código que executam uma tarefa específica.
# Definidas com a palavra-chave "def" seguida do nome e parâmetros opcionais.

# 📌 Quando usar?
# Quando quiser dividir o programa em partes menores e reutilizáveis,
# para evitar repetição e organizar o código.

# 📋 Exemplo 1: Função que apenas executa um print (sem retorno)
print("\n===== FUNÇÕES =====")

def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a).")  # A função imprime diretamente

saudacao("Maria")  # Chamada da função

# 📋 Exemplo 2: Função que retorna um valor com "return"
def soma(a, b):
    return a + b  # A função devolve o valor, mas não imprime

resultado = soma(5, 3)              # Captura o valor retornado
print(f"A soma é: {resultado}")     # Imprime o resultado

# ------------------------------------------------------
# 📌 Diferença entre funções com print e com return:
# ------------------------------------------------------
# - Funções com print() executam a ação dentro da própria função.
#   Ex: saudacao("Maria") já imprime direto.
#
# - Funções com return devolvem o resultado para quem chamou.
#   Ex: soma(5, 3) precisa ser armazenada em uma variável ou usada com print.
#
# ✅ Regra geral:
# - Use print() dentro da função se quiser mostrar algo imediatamente.
# - Use return quando quiser passar o resultado para outra parte do programa.

# ------------------------------------------------------
# ➕ Extras:
# - Funções podem ter mais de um parâmetro.
# - Parâmetros podem ter valores padrão: def exemplo(a, b=2)
# - Funções sem return retornam None por padrão.


