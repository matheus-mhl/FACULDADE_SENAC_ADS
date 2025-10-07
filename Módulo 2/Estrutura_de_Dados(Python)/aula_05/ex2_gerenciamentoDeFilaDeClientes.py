### **Desafio Prático 2: Gerenciamento de Filas de Clientes**

# **Objetivo:** Simular o atendimento de clientes na pizzaria, controlando o fluxo com `for`, `if`, `break` e `enumerate`.

# Instruções:

# A Pizzaria Sabores quer limitar a quantidade de clientes que podem ser atendidos por vez. Crie um sistema para gerenciar a fila.

# 1. **Crie a fila:** Crie uma **lista** chamada `fila_de_espera` com o nome de pelo menos 5 clientes (por exemplo: `["João", "Maria", "Pedro", "Ana", "Carlos"]`).
# 2. **Atenda os clientes:** Use um **loop `for`** para percorrer a lista de clientes.
# 3. **Controle o limite:** Use um **`if`** com a função `enumerate()` para verificar se a pizzaria já atendeu 3 clientes.
# 4. **Encerre o atendimento: Se o limite de 3 clientes for atingido, use o comando break para interromper o loop e exibir uma mensagem informando que "a capacidade máxima de atendimento foi atingida"