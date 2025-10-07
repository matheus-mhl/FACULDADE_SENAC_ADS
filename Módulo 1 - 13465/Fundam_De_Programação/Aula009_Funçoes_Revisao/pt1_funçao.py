def quadrado(n):
    return(n*n)

#programa principal - Main
num=int(input("entre com um numero: "))
print(f'O quadrado de {num} é {quadrado(num)}')

# calcula o resultado da equação y = 4x^2 + 3x^2 + 1
y = 3 * quadrado(num) + 3 * quadrado(num) + 1
print(y)