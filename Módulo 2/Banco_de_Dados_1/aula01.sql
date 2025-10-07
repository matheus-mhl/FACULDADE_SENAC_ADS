--Utilize "--" para comentar.
--Pessoa (CPF Char(11), nome varchar(20), endereco varchar(20), idade int)
--Voce pode utilizar os comandos em maiusculo ou minusculo (CREATE ou create)
CREATE TABLE Pessoa(
CPF char(11),
nome varchar(20),
endereco VarChar(20),
idade int
)

-- Para ler(Serve para visualizar tabela/dados)
select * from Pessoa

--Inserindo Valores
INSERT INTO Pessoa VALUES ('12345678901', 'Matheus', 'Rua Santa Luzia', 26)
INSERT INTO Pessoa VALUES ('92345899901', 'Daniel', 'Rua Santa Luzia', 22)
INSERT INTO Pessoa VALUES ('98745621301', 'Vitor', 'Rua Santa Luzia', 56)

--ALTERAR A TABELA - Inclindo campo e-mail
ALTER TABLE Pessoa ADD EMAIL VARCHAR(20)

INSERT INTO Pessoa VALUES ('99345678901', 'Vitor Merling 123456789', 'Rua Santa Luzia', 40, 'x@emai.com')

-- Alterar o Tamanho da coluna nome
ALTER TABLE Pessoa ALTER COLUMN nome VARCHAR(30)
INSERT INTO Pessoa VALUES ('99345678901', 'Vitor Merling 123456789', 'Rua Santa Luzia', 40, 'x@emai.com')

SELECT * FROM Pessoa;

-- APAGAR Coluna EMAIL
--ALTER TABLE Pessoa DROP COLUMN EMAIL

