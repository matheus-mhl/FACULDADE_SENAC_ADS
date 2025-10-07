#Esse arquivo apresenta exercícios sobre a coleção tipo: DICIONARIO
#----------------------------------------------------------------
#Exercicio SENAC:
# Dicionário - Incrementos ao 
# Projeto TO-DO

# Um aplicativo de lista de tarefas é uma ferramenta útil para organizar tarefas. Crie um programa Python básico,
# que permita aos usuários adicionar, excluir e visualizar tarefas. 

# Use o conceito de listas, onde cada entrada será um elemento da lista.

# Cada entrada será uma frase, e será indexada pelo timestamp (data&hora) da sua criação. 

# Exemplo: 

# {“04-04-2024 13:01”, “Reunião de trabalho”}
#-----------------------------------------------------------------------------------------------------------------------
#RESPOSTA:

#Utilizando "import datetime"
import datetime  # Importa módulo para capturar data e hora

# Criamos um dicionário vazio para armazenar as tarefas
# Chave: timestamp (data e hora) | Valor: descrição da tarefa
tarefas = {}

# Estrutura de repetição infinita: enquanto o usuário não escolher a opção de sair,
# o programa continua executando. Saímos do loop com `break`.
while True:
    # Exibição do menu de opções
    print("\n### Gerenciador de Tarefas ###")
    print("1. Adicionar tarefa")
    print("2. Visualizar todas as tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

    # Lê a opção escolhida pelo usuário
    opcao = input("Selecione a ação desejada (1-4): ")

    # -------------------------------
    # Opção 1: Adicionar uma tarefa
    # -------------------------------
    if opcao == "1":
        nova_tarefa = input("Digite a nova tarefa: ")  # Lê a descrição da tarefa

        # Gera timestamp como string no formato dd-mm-aaaa HH:MM:SS
        agora = datetime.datetime.now()
        timestamp = agora.strftime("%d-%m-%Y %H:%M:%S")

        # Adiciona no dicionário: chave = timestamp, valor = tarefa
        tarefas[timestamp] = nova_tarefa
        print(f"Tarefa adicionada com sucesso! (ID: {timestamp})")

    # -------------------------------
    # Opção 2: Visualizar todas as tarefas
    # -------------------------------
    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nLista de Tarefas:")
            for i, (hora, descricao) in enumerate(tarefas.items(), start=1):
                print(f"{i}. [{hora}] - {descricao}")

    # -------------------------------
    # Opção 3: Remover uma tarefa
    # -------------------------------
    elif opcao == "3":
        if not tarefas:
            print("Nenhuma tarefa para remover.")
        else:
            print("\nTarefas disponíveis para remoção:")
            chaves = list(tarefas.keys())  # Pegamos as chaves em uma lista ordenada
            for i, chave in enumerate(chaves, start=1):
                print(f"{i}. [{chave}] - {tarefas[chave]}")

            try:
                indice = int(input("Digite o número da tarefa a remover: "))
                if 1 <= indice <= len(chaves):
                    chave_remover = chaves[indice - 1]
                    tarefa_removida = tarefas.pop(chave_remover)
                    print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Digite um número válido.")

    # -------------------------------
    # Opção 4: Sair do programa
    # -------------------------------
    elif opcao == "4":
        print("Saindo do programa. Até mais!")
        break  # Encerra o loop e finaliza o programa

    # -------------------------------
    # Opção inválida (fora de 1 a 4)
    # -------------------------------
    else:
        print("Opção inválida. Tente novamente.")

#--------------------------------------------------------------------------------------------------------------------------------------------

# # Utilizando CONTADOR para simular timestamp/ID único
# contador = 1

# tarefas = {}

# while True:
#     print("\n### Gerenciador de Tarefas ###")
#     print("1. Adicionar tarefa")
#     print("2. Visualizar todas as tarefas")
#     print("3. Remover tarefa")
#     print("4. Sair")

#     opcao = input("Selecione a ação desejada (1-4): ")

#     if opcao == "1":
#         nova_tarefa = input("Digite a nova tarefa: ")
#         chave = str(contador)  # ID único como string
#         tarefas[chave] = nova_tarefa
#         print(f"Tarefa adicionada com sucesso! (ID: {chave})")
#         contador += 1  # Incrementa para próxima tarefa

#     elif opcao == "2":
#         if not tarefas:
#             print("Nenhuma tarefa cadastrada.")
#         else:
#             print("\nLista de Tarefas:")
#             for i, (chave, tarefa) in enumerate(tarefas.items(), start=1):
#                 print(f"{i}. [ID {chave}] - {tarefa}")

#     elif opcao == "3":
#         if not tarefas:
#             print("Nenhuma tarefa para remover.")
#         else:
#             print("\nTarefas disponíveis para remoção:")
#             chaves = list(tarefas.keys())
#             for i, chave in enumerate(chaves, start=1):
#                 print(f"{i}. [ID {chave}] - {tarefas[chave]}")

#             try:
#                 indice = int(input("Digite o número da tarefa a remover: "))
#                 if 1 <= indice <= len(chaves):
#                     chave_remover = chaves[indice - 1]
#                     tarefa_removida = tarefas.pop(chave_remover)
#                     print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
#                 else:
#                     print("Número inválido.")
#             except ValueError:
#                 print("Digite um número válido.")

#     elif opcao == "4":
#         print("Saindo do programa. Até mais!")
#         break

#     else:
#         print("Opção inválida. Tente novamente.")

