**Tipos de violações de restrição em Banco de Dados**



🧩 1. Violação de restrição de domínio



O que é: ocorre quando o valor inserido em uma coluna não pertence ao domínio permitido (tipo, intervalo, formato, etc.).



Exemplo:



INSERT INTO Aluno (idade) VALUES ('dezesseis');





🔴 Erro: a coluna idade aceita apenas números inteiros, e foi inserido texto.



🧱 2. Violação de integridade (ou integridade de entidade)



O que é: acontece quando a chave primária (PRIMARY KEY) é nula ou duplicada, o que quebra a identificação única de cada registro.



Exemplo:



INSERT INTO Cliente (id\_cliente, nome) VALUES (NULL, 'Ana');





🔴 Erro: o id\_cliente é chave primária, não pode ser nulo.



🔗 3. Violação de integridade referencial



O que é: ocorre quando uma chave estrangeira (FOREIGN KEY) aponta para um registro que não existe na tabela referenciada.



Exemplo:



INSERT INTO Pedido (id\_cliente) VALUES (999);





🔴 Erro: o id\_cliente = 999 não existe na tabela Cliente.



⚙️ 4. Violação de restrições definidas pelo usuário



O que é: são regras criadas manualmente pelo desenvolvedor para garantir condições específicas de negócio.



Exemplo:



ALTER TABLE Funcionario

ADD CONSTRAINT chk\_salario CHECK (salario > 0);





E depois:



INSERT INTO Funcionario (salario) VALUES (-500);





🔴 Erro: o salário viola a regra definida pelo usuário (salario > 0).

