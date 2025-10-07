/*Exerc�cios de Cria��o de Tabelas (DDL)
Nesta atividade voc� est� respons�vel por construir um Database para uma livraria. Considere que a an�lise realizada levou a um esquema com 5 tabelas, descritas a seguir. 
N�o esque�a de criar um database (por exemplo, �LIVRARIA�) para hospedar estas tabelas.
1.	Tabela de Editoras
Crie uma tabela chamada Editoras para armazenar informa��es sobre as casas editoriais.
Requisitos:
�	id_editora: Chave prim�ria de tipo INT.
�	nome: String de at� 100 caracteres, n�o pode ser nulo.
�	cidade: String de at� 50 caracteres, n�o pode ser nulo.
�	pais: String de at� 50 caracteres, com um valor padr�o de 'Brasil'.*/

CREATE TABLE Editoras(
id_editora INT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
cidade VARCHAR(50) NOT NULL,
pais VARCHAR(50) DEFAULT 'Brasil'
);

/*2.	Tabela de Autores
Crie uma tabela chamada Autores para registrar os escritores.
Requisitos:
�	id_autor: Chave prim�ria de tipo INT.
�	nome: String de at� 100 caracteres, n�o pode ser nulo.
�	data_nascimento: Data, n�o pode ser nula.
�	email: String de at� 150 caracteres, n�o pode ser nulo, e deve ser �nico.*/

CREATE TABLE Autores(
id_autor INT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
data_nascimento DATE NOT NULL,
email VARCHAR(150) NOT NULL UNIQUE
);

/*3.	Tabela de Livros
Crie uma tabela chamada Livros para catalogar os livros dispon�veis.
Requisitos:
�	id_livro: Chave prim�ria de tipo INT.
�	titulo: String de at� 200 caracteres, n�o pode ser nulo.
�	ano_publicacao: N�mero inteiro, n�o pode ser nulo, e deve ser maior que 1900.
�	isbn: String de 13 caracteres, n�o pode ser nulo, e deve ser �nico.
�	id_editora: N�mero inteiro, n�o pode ser nulo, e deve ser uma chave estrangeira que referencia a tabela Editoras.*/

CREATE TABLE Livros(
id_livro INT PRIMARY KEY,
titulo VARCHAR(200) NOT NULL,
ano_publicacao INT NOT NULL CHECK(ano_publicacao > 1900),
isbn VARCHAR(13) NOT NULL UNIQUE,
id_editora INT NOT NULL,
FOREIGN KEY(id_editora) REFERENCES Editoras(id_editora)
);

/*4.	Tabela de Avalia��es
Crie uma tabela chamada Avaliacoes para registrar as notas e coment�rios dos usu�rios sobre os livros.
Requisitos:
�	id_avaliacao: Chave prim�ria de tipo INT.
�	id_livro: N�mero inteiro, n�o pode ser nulo, e deve ser uma chave estrangeira que referencia a tabela Livros.
�	nota: N�mero inteiro, n�o pode ser nulo, e deve ser entre 1 e 5.
�	comentario: String de at� 500 caracteres, que pode ser nula.*/

CREATE TABLE Avalia��es(
id_avaliacao INT PRIMARY KEY,
id_livro INT NOT NULL,
nota INT NOT NULL CHECK(nota BETWEEN 1 AND 5),
comentario VARCHAR(500) NULL,
FOREIGN KEY(id_livro) REFERENCES Livros(id_livro) --A FOREIGN KEY deve ser escrita na ultima linha(apenas uma BOA PRATICA)
);

/*5. Tabela Autores_Livros
Crie uma tabela de liga��o chamada Autores_Livros para conectar autores a livros, 
j� que um livro pode ter v�rios autores e um autor pode ter v�rios livros.
Requisitos:
id_autor: N�mero inteiro, n�o pode ser nulo, e deve ser uma chave estrangeira que referencia a tabela Autores.
id_livro: N�mero inteiro, n�o pode ser nulo, e deve ser uma chave estrangeira que referencia a tabela Livros.
A chave prim�ria deve ser a combina��o de (id_autor, id_livro).*/

CREATE TABLE Autores_Livros(
id_autor INT NOT NULL,
id_livro INT NOT NULL,
FOREIGN KEY(id_autor) REFERENCES Autores(id_autor),
FOREIGN KEY(id_livro) REFERENCES Livros(id_livro),
 PRIMARY KEY(id_autor, id_livro)
 );

/*6. Comando INSERT (Inserindo Dados)
Inserir uma Nova Editora: Adicione uma nova editora � tabela Editoras.
(101, 'Editora Z', 'Curitiba', 'Brasil');
Inserir um Novo Autor:
(201, 'Ana Luiza Souza', '1985-02-28', 'ana.souza@escritores.com.br');
Adicione um livro que foi publicado pela Editora Z.
(301, 'Aventuras na Montanha', 2022, '978-85-12345-67-8', 101)
Use a tabela de jun��o Autores_Livros para associar 'Ana Luiza Souza' ao livro 'Aventuras na Montanha'. 
Inserir uma Avalia��o: Adicione uma avalia��o para o livro 'Aventuras na Montanha', com nota 5.
(401, 301, 5, 'Uma leitura incr�vel e emocionante!')*/

INSERT INTO Editoras(id_editora, nome, cidade, pa�s)
VALUES (101, 'Editora Z', 'Curitiba', 'Brasil');
INSERT INTO Autores(id_autor, nome, data_nascimento, email)
VALUES (201, 'Ana Luiza Souza', '1985-02-28', 'ana.souza@escritores.com.br');
INSERT INTO Livros (id_livro, titulo, ano_publicacao, isbn, id_editora)
VALUES (301, 'Aventuras na Montanha', 2022, '978-85-12345-67-8', 101); 
INSERT INTO Autores_Livros(id_autor,id_livro)
VALUES (201,301);
INSERT Avalia��es(id_avaliacao, id_avaliacao, nota, comentario)
VALUES (401, 301, 5, 'Uma leitura incr�vel e emocionante!');

/*7. Comando SELECT (Leitura/Consulta de Dados)
Listar Todos os Livros: Recupere o t�tulo, ano de publica��o e ISBN de todos os livros.
Encontrar Livros por Ano de Publica��o: Liste todos os livros publicados ap�s o ano 2000.
Comando UPDATE (Alterando Dados)
Corrigir um T�tulo: Altere o t�tulo do livro 'Aventuras na Montanha' para 'Aventuras na Montanha M�gica'.
Aumentar o N�mero de Avalia��es: Em um cen�rio de e-commerce, a m�dia de avalia��es de um livro pode ser atualizada. 
Altere a nota da avalia��o para 4, supondo que a m�dia da nota desse livro agora � essa.*/

SELECT Livros, ano_publicacao, isbn FROM Livros; -- Listando livros


/*8. Comando UPDATE (Alterando Dados)
Corrigir um T�tulo: Altere o t�tulo do livro 'Aventuras na Montanha' para 'Aventuras na Montanha M�gica'.
Aumentar o N�mero de Avalia��es: Em um cen�rio de e-commerce, a m�dia de avalia��es de um livro pode ser atualizada.
Altere a nota da avalia��o para 4, supondo que a m�dia da nota desse livro agora � essa.*/

/*9. Comando DELETE (Apagando Dados)
Remover uma Avalia��o: Exclua a avalia��o que voc� inseriu.
Excluir um Livro e sua Rela��o com o Autor: Voc� precisa deletar o livro 'Aventuras na Montanha' da base de dados. 
Lembre-se que voc� precisa primeiro remover a entrada na tabela Autores_Livros antes de poder remover o livro da tabela Livros.*/







