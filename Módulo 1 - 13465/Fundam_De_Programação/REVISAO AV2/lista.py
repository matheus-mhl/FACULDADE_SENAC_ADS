#Esse arquivo apresenta exercícios sobre a coleção tipo: LISTAS
#----------------------------------------------------------------
#Exercicio SENAC:
# Projeto TO-DO – usando Listas

# Um aplicativo de lista de tarefas é uma ferramenta útil para organizar tarefas. Crie um programa Python básico,
# que permita aos usuários adicionar, excluir e visualizar tarefas. 

# Neste exercício, você construirá um programa simples para gerenciar suas tarefas diárias.

# Criar um programa Python que permita:

# Adicionar uma nova tarefa à lista.
# Visualizar todas as tarefas 
# Remover uma tarefa da lista.

# Exemplo da tela inicial:

# ### Gerenciador de Tarefas ###
# 1. Adicionar tarefa
# 2. Visualizar todas as tarefas
# 3. Remover tarefa
# 4. Sair

#-----------------------------------------------------------------

#RESPOSTA:

# Gerenciador de Tarefas usando Listas
# Exercício proposto: Adicionar, visualizar e remover tarefas
# -----------------------------------------

# -----------------------------------------
# Gerenciador de Tarefas usando Listas
# Exercício proposto: Adicionar, visualizar e remover tarefas
# -----------------------------------------

# Criamos uma lista vazia para armazenar as tarefas.
tarefas = []

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
        tarefas.append(nova_tarefa)  # Adiciona a tarefa à lista
        print("Tarefa adicionada com sucesso!")

    # -------------------------------
    # Opção 2: Visualizar todas as tarefas
    # -------------------------------
    elif opcao == "2":
        if not tarefas:
            # A lista está vazia
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nLista de Tarefas:")
            # `enumerate` é usado para numerar as tarefas (começando em 1)
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")

    # -------------------------------
    # Opção 3: Remover uma tarefa
    # -------------------------------
    elif opcao == "3":
        if not tarefas:
            print("Nenhuma tarefa para remover.")
        else:
            print("\nTarefas disponíveis para remoção:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")
            try:
                # O usuário deve digitar o número da tarefa a ser removida
                indice = int(input("Digite o número da tarefa a remover: "))

                # Verifica se o número está dentro do intervalo válido
                if 1 <= indice <= len(tarefas):
                    # Remove a tarefa com base no índice fornecido (ajustado para 0 baseado)
                    tarefa_removida = tarefas.pop(indice - 1)
                    print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
                else:
                    print("Número inválido.")  # Número fora do intervalo da lista
            except ValueError:
                # Caso o usuário digite algo que não seja número
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
        
    #-----------------------------------------------------------------------------------------------------------------------


