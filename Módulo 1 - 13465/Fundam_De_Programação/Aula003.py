#Nessa aula aprendemos sobre: STRINGS
# print("Isso é uma STRING")

# Indexação e substrings
# Variáveis do tipo string armazenam cadeias de caracteres como nomes e textos. A string pode ser visualizada como um vetor/lista armazenando caracteres:
# Podemos acessar os caracteres da string como em um vetor: 
# Exemplo:
# str = ("A casa azul")
# print (str)
# print (str[0]) 	# “A”
# print (str [2:6])#print  #”casa” observe que não inclui o 6º 
# print (str[2])
# print (str[0:4])
 
#Exercício 1 - Faça um programa que peça seu nome e imprima “bem-vindo a programação Python fulano!”.

# nome = str(input("Digite seu nome:"))
# print (f"bem-vindo a programação Python {nome}!")

#Exercício 2 - Faça um programa em Python que leia uma string aleatória com no mínimo 20 caracteres quaisquer e forneça 
# a)Seu tamanho, 
# b)Quantidade total de letras/números/símbolos
# c)Quantidade total de ocorrência do primeiro caractere
# d)Imprima uma versão maiúscula e uma minúscula da string

# string = str("A vida é bela sempre.") 
# #a)
# print (string)
# #b)
# print ((len(string)))
# #c)
# print (len(string [0]))
# #d)
# print (string.lower()) #versão minúscula
# print (string.upper()) #versão maiúscula

#AGORA É COM VOCÊS
#Exercício 3 - Faça um programa que leia um nome e imprima as 4 primeiras letras do nome.
# Nome = str(input("Me diga seu nome:"))
# print (f"Olá {Nome}!!")
# print (f"As primeiras quatro letras do seu nome são: {Nome [0:4]}!!")

#Exercício 4 - Escreva um programa que substitui as ocorrências de um caractere 0 em uma string por outro caractere 1. Testar com 'De 0 a 100 voce é nota 1000'
# text = 'De 0 a 100 voce é nota 1000'
# text_modified = text.replace('0', '1')
# print (text_modified)

#Exercício 5 - Entre com um nome e imprima o nome somente se a primeira letra do nome for “a” (maiúscula ou minúscula).
# Nome = str(input("Digite seu nome:"))
# if Nome [0] == str("A"):
#     print (Nome)
# elif Nome [0] == str("a"):
#     print (Nome)
# else:
#     print ("Sinto muito, mas esse nome não começa com a letra 'A'...")

#SEGUNDA OPÇÃO DE RESOLUÇÃO PARA Exercicio 5
# nome=input("Entre com um nome: ")
# if nome[0].lower() == 'a':
#     print(nome)
# else:
#     print("Nome inválido")

#Exercicio 6 - Faça um programa que receba do usuário uma string. O programa imprime a string sem suas vogais.
# string = str(input("Digite o que quiser:")) 
# vogais = "aeiouAEIOU"
# string_sem_vogais = ""
# for letra in string:
#      if letra not in vogais:
#          string_sem_vogais = string_sem_vogais + letra
# print("String sem vogais:", string_sem_vogais)

#Exercicio 7 - Faça um programa que receba um texto e calcule quantas vogais (‘a’, ‘e’, ‘i’, ‘o’, ‘u’) possui essa palavra. 
# texto = str(input("Digite um texto:"))
# vogais = "aeiouAEIOU"
# contador_de_vogais = 0
# for letras in texto:
#      if letras in vogais:
#          contador_de_vogais += 1
# print(f"O número de vogais contidas no texto é de: {contador_de_vogais}")



#Exercício 8 - Com o programa anterior, faça um código que substitua todas as vogais do texto dado por 'x'.
texto = str(input("Digite um texto:"))
vogais = "aeiouAEIOU"
vogaisX = ""
for vogais in texto:
    vogaisX = texto - vogais
print(f"Texto substituindo vogais por X -->{vogaisX}")
#CORRIGIR SOLUÇÃO ACIMA^^^^^!!!!!!!!!!!!!

#Segunda forma de resolver o exercicio 8:
# nome= input("Entre com um nome")
# nome.replace('a','x')
# nome.replace('e','x')
# nome.replace('i','x')
# nome.replace('o','x')
# nome.replace('u','x')
# nome.replace('A','x')
# nome.replace('E','x')
# nome.replace('I','x')
# nome.replace('O','x')
# nome.replace('U','x')
# print(nome)




