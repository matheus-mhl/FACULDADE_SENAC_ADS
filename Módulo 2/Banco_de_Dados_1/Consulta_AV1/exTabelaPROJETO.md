/*1. Crie uma tabela PROJETO com as seguintes colunas:
PROJNO - número do projeto (número inteiro, chave primária, não nulo)
PRONOME - nome do projeto (até 10 caracteres, não nulo)
DATAINICIO - data de início do projeto (não nulo)
DESCRICAO - descrição do projeto (até 50 caracteres)
*/

CREATE TABLE PROJETO(
    PROJNO INT PRIMARY KEY NOT NULL, -- chave primária
    PRONOME VARCHAR(10) NOT NULL,    -- nome obrigatório
    DATAINICIO DATE NOT NULL,        -- data obrigatória
    DESCRICAO VARCHAR(50)            -- descrição opcional
);

-- Comando para visualizar tabela criada
SELECT * FROM PROJETO;


/*2. Crie uma tabela EQUIPE de acordo com a descrição: 
EQNO - número da equipe (número inteiro) 
EQNOME - nome da equipe com até 10 caracteres

Na declaração de criação, defina a CHAVE PRIMARIA EQUIPE_PK na coluna EQNO.
Não permita que as seguintes colunas tenham valores NULOS: EQNOME
*/

CREATE TABLE EQUIPE(
    EQNO INT PRIMARY KEY,     -- chave primária
    EQNOME VARCHAR(10) NOT NULL -- nome obrigatório
);


/*3. Na tabela PROJETO, adicione uma coluna EQNO (número da equipe - número inteiro) para uma equipe que trabalha no projeto.*/

ALTER TABLE PROJETO
ADD EQNO INT;


/*4. Defina a coluna EQNO da tabela PROJETO como uma chave estrangeira denominada PRO_TM_FK para a tabela EQUIPE.*/

ALTER TABLE PROJETO
ADD CONSTRAINT PRO_TM_FK
FOREIGN KEY (EQNO)
REFERENCES EQUIPE (EQNO);


/*5. Insira os seguintes registros para PROJETO:
- projeto denominado 'MATRIX', iniciando na data atual, número 100
- projeto denominado 'ABC', iniciando no dia seguinte, número 200, descrição 'Temporário'
- projeto denominado 'PREMIUM', iniciando no dia seguinte, número 300, descrição 'Estratégico'

Deixe o campo referente à equipe como NULL
*/

INSERT INTO PROJETO (PROJNO, PRONOME, DATAINICIO, DESCRICAO, EQNO)
VALUES
  (100, 'MATRIX', '2025-10-05', NULL, NULL),
  (200, 'ABC', '2025-10-06', 'Temporário', NULL),
  (300, 'PREMIUM', '2025-10-06', 'Estratégico', NULL);

-- Selecionar conteúdo da tabela
SELECT * FROM PROJETO;


/*6. Atualize a descrição do projeto 100 para 'Projeto experimental';*/

UPDATE PROJETO
SET DESCRICAO = 'Projeto experimental'
WHERE PROJNO = 100;

-- Selecionar conteúdo atualizado
SELECT * FROM PROJETO;


/*7. Remova o projeto 'Temporário' (assumindo que os projetos são identificados por seus números)*/

DELETE FROM PROJETO
WHERE PROJNO = 200;

-- Selecionar conteúdo da tabela após remoção
SELECT * FROM PROJETO;


/*8. Insira os seguintes registros para EQUIPE:
- Equipe denominada 'BLACKBELT', código 10
- Equipe denominada 'BROWNBELT', código 11
- Equipe denominada 'WHITEBELT', código 12
*/

INSERT INTO EQUIPE (EQNO, EQNOME)
VALUES
  (10, 'BLACKBELT'),
  (11, 'BROWNBELT'),
  (12, 'WHITEBELT');

-- Selecionar conteúdo da tabela EQUIPE
SELECT * FROM EQUIPE;


/*9. Associe o projeto 'MATRIX' à equipe 'BLACKBELT' e o projeto 'PREMIUM' à equipe 'BROWNBELT';*/

UPDATE PROJETO
SET EQNO = 10
WHERE PRONOME = 'MATRIX';

UPDATE PROJETO
SET EQNO = 11
WHERE PRONOME = 'PREMIUM';

-- Verificar associação
SELECT * FROM PROJETO;


/*10. Na tabela PROJETO, adicione uma coluna PROJVERBA, com restrição CHK_VERBA sendo um número inteiro positivo*/

ALTER TABLE PROJETO
ADD PROJVERBA INT;

ALTER TABLE PROJETO
ADD CONSTRAINT CHK_VERBA CHECK (PROJVERBA > 0);


/*11. Na tabela EQUIPE, adicione uma coluna ORIGEM tipo CHAR, com restrição de domínio CHK_ORIGEM, aceitando apenas os valores 'I' ou 'E' (Interno ou Externo)*/

ALTER TABLE EQUIPE
ADD ORIGEM CHAR(1);

ALTER TABLE EQUIPE
ADD CONSTRAINT CHK_ORIGEM CHECK (ORIGEM IN ('I','E'));


/*12. Remova todas as tabelas criadas*/

DROP TABLE PROJETO CASCADE CONSTRAINTS;
DROP TABLE EQUIPE CASCADE CONSTRAINTS;
