# Desenvolva uma função que calcule a área de um retângulo.A função será “calcular_area_retangulo(base, altura)”, 
# que recebe dois números, base e altura, como argumentos e retorna o valor da área (base*altura).

def calcular_area_retangulo(base, altura):
    return(base*altura)

#Main - programa principal
base=int(input("Digite o valor da BASE do retângulo: "))
altura=int(input("Digite o valor da ALTURA do retângulo: "))
area= calcular_area_retangulo(base, altura)

print(f'A área do retângulo é de: {base} * {altura } = {area}')


