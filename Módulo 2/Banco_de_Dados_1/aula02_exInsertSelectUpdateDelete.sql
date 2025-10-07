INSERT INTO pacientes VALUES --Inserindo valores
(999, 'Fernando', '12300008911', 'M', 55, 'Teresópolis', 'Febre Amarela')

SELECT * FROM pacientes --Visualizar tabela 'paceintes'
UPDATE pacientes SET idade = 45 WHERE codp=999 --ATUALIZANDO tabela

INSERT INTO consultas VALUES (30, 999, '2020-04-25', '08:30:00')--Inserindo valores

SELECT * FROM consultas
UPDATE consultas SET hora = '14:30:00' WHERE codp=999 --Atualizando tabela

DELETE FROM consultas WHERE codp=999 --Deletando linha da tabela
