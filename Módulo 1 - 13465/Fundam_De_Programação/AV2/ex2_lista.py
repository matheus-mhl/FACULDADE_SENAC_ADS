# Questão 2: Listas e Estruturas de Repetição

# Crie um programa contendo uma lista vazia chamada “minhas_tarefa_diarias”. 
# Permita ao usuário adicionar até 5 tarefa a lista, informando se cada uma 
# está "concluída" ou "pendente". # Salve as tarefa como strings formatadas, 
# por exemplo: "Estudar Python - pendente". 
# Em seguida, exiba todas as tarefa enumeradas. 
# Então crie uma segunda lista chamada tarefa_pendentes com apenas as tarefa 
# marcadas como "pendente" e, ao final, mostre essa lista ou informe 
# que não há tarefa pendentes.

#RESPOSTA
#Lista:
minhas_tarefas_diarias = []

print("Adicione até 5 tarefas: ")

for i in range (5):
    nome = input(f"Digite tarefa desejada {i + 1}: ")
    concluida_ou_pendente = input(f"Informe se a tarefa foi CONCLUÍDA ou se está PENDENTE: ")
    
    tarefas_do_dia = f"{nome} - {concluida_ou_pendente}"
    minhas_tarefas_diarias.append(tarefas_do_dia)
    
    print("\n---Tarefas Diárias---")
    for sequencia, tarefas in enumerate(minhas_tarefas_diarias):
        #enumerate...
        print(f"{sequencia} - {tarefas}")
        
    tarefas_pendentes = []
    for tarefas in tarefas_do_dia:
        if "pendente" in tarefas:
            tarefas_pendentes.append(tarefas)
        
print("\n---Tarefas Pendentes---")  
if tarefas_pendentes:
    for pendente in tarefas_pendentes:
        print(f"{pendente}")
    else:
        print("Sem tarefas pendentes.")    
    