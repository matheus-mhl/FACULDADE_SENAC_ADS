/*Exercícios de Criação de Tabelas (DDL)
Nesta atividade você está responsável por construir um Database para uma livraria. Considere que a análise realizada levou a um esquema com 5 tabelas, descritas a seguir. 
Não esqueça de criar um database (por exemplo, ‘LIVRARIA’) para hospedar estas tabelas.
1.	Tabela de Editoras
Crie uma tabela chamada Editoras para armazenar informações sobre as casas editoriais.
Requisitos:
•	id_editora: Chave primária de tipo INT.
•	nome: String de até 100 caracteres, não pode ser nulo.
•	cidade: String de até 50 caracteres, não pode ser nulo.
•	pais: String de até 50 caracteres, com um valor padrão de 'Brasil'.*/

CREATE TABLE Editoras(
id_editora INT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
cidade VARCHAR(50) NOT NULL,
pais VARCHAR(50) DEFAULT 'Brasil'
);

/*2.	Tabela de Autores
Crie uma tabela chamada Autores para registrar os escritores.
Requisitos:
•	id_autor: Chave primária de tipo INT.
•	nome: String de até 100 caracteres, não pode ser nulo.
•	data_nascimento: Data, não pode ser nula.
•	email: String de até 150 caracteres, não pode ser nulo, e deve ser único.*/

CREATE TABLE Autores(
id_autor INT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
data_nascimento DATE NOT NULL,
email VARCHAR(150) NOT NULL UNIQUE
);

/*3.	Tabela de Livros
Crie uma tabela chamada Livros para catalogar os livros disponíveis.
Requisitos:
•	id_livro: Chave primária de tipo INT.
•	titulo: String de até 200 caracteres, não pode ser nulo.
•	ano_publicacao: Número inteiro, não pode ser nulo, e deve ser maior que 1900.
•	isbn: String de 13 caracteres, não pode ser nulo, e deve ser único.
•	id_editora: Número inteiro, não pode ser nulo, e deve ser uma chave estrangeira que referencia a tabela Editoras.*/

CREATE TABLE Livros(
id_livro INT PRIMARY KEY,
titulo VARCHAR(200) NOT NULL,
ano_publicacao INT NOT NULL CHECK(ano_publicacao > 1900),
isbn VARCHAR(13) NOT NULL UNIQUE,
id_editora INT NOT NULL,
FOREIGN KEY(id_editora) REFERENCES Editoras(id_editora)
);

/*4.	Tabela de Avaliações
Crie uma tabela chamada Avaliacoes para registrar as notas e comentários dos usuários sobre os livros.
Requisitos:
•	id_avaliacao: Chave primária de tipo INT.
•	id_livro: Número inteiro, não pode ser nulo, e deve ser uma chave estrangeira que referencia a tabela Livros.
•	nota: Número inteiro, não pode ser nulo, e deve ser entre 1 e 5.
•	comentario: String de até 500 caracteres, que pode ser nula.*/

CREATE TABLE Avaliações(
id_avaliacao INT PRIMARY KEY,
id_livro INT NOT NULL,
nota INT NOT NULL CHECK(nota BETWEEN 1 AND 5),
comentario VARCHAR(500) NULL,
FOREIGN KEY(id_livro) REFERENCES Livros(id_livro) --A FOREIGN KEY deve ser escrita na ultima linha(apenas uma BOA PRATICA)
);

/*5. Tabela Autores_Livros
Crie uma tabela de ligação chamada Autores_Livros para conectar autores a livros, 
já que um livro pode ter vários autores e um autor pode ter vários livros.
Requisitos:
id_autor: Número inteiro, não pode ser nulo, e deve ser uma chave estrangeira que referencia a tabela Autores.
id_livro: Número inteiro, não pode ser nulo, e deve ser uma chave estrangeira que referencia a tabela Livros.
A chave primária deve ser a combinação de (id_autor, id_livro).*/

CREATE TABLE Autores_Livros(
id_autor INT NOT NULL,
id_livro INT NOT NULL,
FOREIGN KEY(id_autor) REFERENCES Autores(id_autor),
FOREIGN KEY(id_livro) REFERENCES Livros(id_livro),
 PRIMARY KEY(id_autor, id_livro)
 );

/*6. Comando INSERT (Inserindo Dados)
Inserir uma Nova Editora: Adicione uma nova editora à tabela Editoras.
(101, 'Editora Z', 'Curitiba', 'Brasil');
Inserir um Novo Autor:
(201, 'Ana Luiza Souza', '1985-02-28', 'ana.souza@escritores.com.br');
Adicione um livro que foi publicado pela Editora Z.
(301, 'Aventuras na Montanha', 2022, '978-85-12345-67-8', 101)
Use a tabela de junção Autores_Livros para associar 'Ana Luiza Souza' ao livro 'Aventuras na Montanha'. 
Inserir uma Avaliação: Adicione uma avaliação para o livro 'Aventuras na Montanha', com nota 5.
(401, 301, 5, 'Uma leitura incrível e emocionante!')*/

INSERT INTO Editoras(id_editora, nome, cidade, país)
VALUES (101, 'Editora Z', 'Curitiba', 'Brasil');
INSERT INTO Autores(id_autor, nome, data_nascimento, email)
VALUES (201, 'Ana Luiza Souza', '1985-02-28', 'ana.souza@escritores.com.br');
INSERT INTO Livros (id_livro, titulo, ano_publicacao, isbn, id_editora)
VALUES (301, 'Aventuras na Montanha', 2022, '978-85-12345-67-8', 101); 
INSERT INTO Autores_Livros(id_autor,id_livro)
VALUES (201,301);
INSERT Avaliações(id_avaliacao, id_avaliacao, nota, comentario)
VALUES (401, 301, 5, 'Uma leitura incrível e emocionante!');

/*7. Comando SELECT (Leitura/Consulta de Dados)
Listar Todos os Livros: Recupere o título, ano de publicação e ISBN de todos os livros.
Encontrar Livros por Ano de Publicação: Liste todos os livros publicados após o ano 2000.
Comando UPDATE (Alterando Dados)
Corrigir um Título: Altere o título do livro 'Aventuras na Montanha' para 'Aventuras na Montanha Mágica'.
Aumentar o Número de Avaliações: Em um cenário de e-commerce, a média de avaliações de um livro pode ser atualizada. 
Altere a nota da avaliação para 4, supondo que a média da nota desse livro agora é essa.*/

SELECT Livros, ano_publicacao, isbn FROM Livros; -- Listando livros


/*8. Comando UPDATE (Alterando Dados)
Corrigir um Título: Altere o título do livro 'Aventuras na Montanha' para 'Aventuras na Montanha Mágica'.
Aumentar o Número de Avaliações: Em um cenário de e-commerce, a média de avaliações de um livro pode ser atualizada.
Altere a nota da avaliação para 4, supondo que a média da nota desse livro agora é essa.*/

/*9. Comando DELETE (Apagando Dados)
Remover uma Avaliação: Exclua a avaliação que você inseriu.
Excluir um Livro e sua Relação com o Autor: Você precisa deletar o livro 'Aventuras na Montanha' da base de dados. 
Lembre-se que você precisa primeiro remover a entrada na tabela Autores_Livros antes de poder remover o livro da tabela Livros.*/







