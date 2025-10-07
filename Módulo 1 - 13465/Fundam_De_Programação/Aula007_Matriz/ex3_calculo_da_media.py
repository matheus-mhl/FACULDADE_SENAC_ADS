# 3 - Dada a matriz de alunos e notas, calcular a media de cada aluno e informar se ele passou (>=6) ou foi reprovado (<6)
alunos = 'Ana', 'João', 'Carla', 'Aline', 'Pedro'
notas = [
    [10.0, 7.5, 4.3, 8.2, 6.0],
    [9.5, 8.0, 3.6, 7.8, 9.0],
    [6.5, 4.9, 5.7, 6.0, 7.2],
    [3.5, 1.0, 5.0, 3.6, 4.4],
    [10.0, 9.0, 9.5, 8.9, 9.2]
]

media = 0

for i in range(5):
    media = sum(notas[i])/len(notas[i])
    if media >= 6:
        print(f"{alunos[i]}: APROVADO")
    else:
        print(f"{alunos[i]}: REPROVADO")

#ATIVIDADE INCOMPLETA