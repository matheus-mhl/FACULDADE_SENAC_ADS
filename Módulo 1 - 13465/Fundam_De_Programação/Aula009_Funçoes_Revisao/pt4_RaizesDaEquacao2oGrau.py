#Revisar o codigo abaixo. A ideia é tentar desenvolver um programa que me de o resultado da raiz de uma equação de segundo grau.
import math

def leParametro(letra):
    numero=int(input(f'Entre com o parametro {letra}: '))
    return(numero)
def telaInicial():
    while True:
        print('----- RAIZES DA EQUACAO DO 2o GRAU A.X^2 + B.X + C = 0 -----')
        print('Entre com os parametros A, B e C:')
        A = leParametro('A')
        B = leParametro('B')
        C = leParametro('C')
        
        return(A, B, C)
    
def calculaRaizes(parA, parB, parC):
    if parA == 0:
        print('Erro: O parametro A nao pode ser ZERO!!!')
    
    delta = math.pow(parB,2)-4*parA*parC
    if delta < 0:
        print('Erro: Raízes complexas!!!')
    elif delta == 0:
        print('raiz unica')
        raiz1=b/2*parA
        raiz2=raiz1
    else:
        raiz1=(-parB + math.sqrt(delta))/(2*parA)
        raiz2=(-parB + math.sqrt(delta))/(2*parA)
        
    return(True, raiz1, raiz2)
            