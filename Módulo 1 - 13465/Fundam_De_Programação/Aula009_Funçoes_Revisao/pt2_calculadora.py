def soma(x1, x2):
    return(x1 + x2)

def subtracao(x1, x2):
    return(x1 - x2)

def telaInicial():
    while True:
        print('-----CALCULADORA BASICA-----')
        print('Entre com a operação desejada:')
        opcao=input('Adicao/Subtracao/Fim (A/S/X): ')
        if opcao.upper() in ('A', 'S', 'X'):
            return(opcao.upper())
            break
        else:
            print('Opção Inválida!!')

def leNumero():
    numero=int(input("entre com o numro: "))
    return(numero)

#main
while True: #Utilizando "while True" para determinar o seguinte código como Verdadeiro 
    oper=telaInicial
    if oper=='X':
        break
    num1=leNumero()
    num2=leNumero()
    if oper=='S':
        print(f'{num1} + {num2} = {soma(num1,num2)}')
    else:
        print(f'{num1} - {num2} = {subtracao(num1,num2)}')
    
#Fim do programa
print('Fechando a Calculadora')