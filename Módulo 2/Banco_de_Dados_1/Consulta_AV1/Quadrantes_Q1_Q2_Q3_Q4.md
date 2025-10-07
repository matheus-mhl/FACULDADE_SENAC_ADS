🧩 1. Criação das tabelas

Cada quadrante tem uma tabela (Q1, Q2, Q3, Q4), e cada uma armazena coordenadas (x, y).

CREATE TABLE Q1 (
  x INT NOT NULL,
  y INT NOT NULL
);

CREATE TABLE Q2 (
  x INT NOT NULL,
  y INT NOT NULL
);

CREATE TABLE Q3 (
  x INT NOT NULL,
  y INT NOT NULL
);

CREATE TABLE Q4 (
  x INT NOT NULL,
  y INT NOT NULL
);


📘 Lembrete:

Q1: x > 0 e y > 0

Q2: x < 0 e y > 0

Q3: x < 0 e y < 0

Q4: x > 0 e y < 0

🧮 2. Inserindo as coordenadas

Temos que verificar em qual quadrante cada coordenada pertence antes de inserir.

Exemplo:

Coordenada (x,y)	Quadrante
(1,10)	Q1
(-10,8)	Q2
(-10,-18)	Q3
(18,-9)	Q4
(-1,-10)	Q3
(10,8)	Q1
(-10,18)	Q2
(-18,9)	Q2
(-1,10)	Q2
(-10,9)	Q2
(10,18)	Q1
(9,19)	Q1
(20,10)	Q1
(-21,11)	Q2
(-22,-12)	Q3
(20,-10)	Q4

Então os INSERTs seriam:

-- Q1 (x > 0, y > 0)
INSERT INTO Q1 VALUES (1,10), (10,8), (10,18), (9,19), (20,10);

-- Q2 (x < 0, y > 0)
INSERT INTO Q2 VALUES (-10,8), (-10,18), (-18,9), (-1,10), (-10,9), (-21,11);

-- Q3 (x < 0, y < 0)
INSERT INTO Q3 VALUES (-10,-18), (-1,-10), (-22,-12);

-- Q4 (x > 0, y < 0)
INSERT INTO Q4 VALUES (18,-9), (20,-10);

🧱 3. Inserir nova coluna z
ALTER TABLE Q1 ADD COLUMN z INT;
ALTER TABLE Q2 ADD COLUMN z INT;
ALTER TABLE Q3 ADD COLUMN z INT;
ALTER TABLE Q4 ADD COLUMN z INT;

🔁 4. Atualizar z

Regra:

se x for ímpar → z = -1

se x for par → z = 1

UPDATE Q1 SET z = CASE WHEN x % 2 <> 0 THEN -1 ELSE 1 END;
UPDATE Q2 SET z = CASE WHEN x % 2 <> 0 THEN -1 ELSE 1 END;
UPDATE Q3 SET z = CASE WHEN x % 2 <> 0 THEN -1 ELSE 1 END;
UPDATE Q4 SET z = CASE WHEN x % 2 <> 0 THEN -1 ELSE 1 END;

❌ 5. Apagar linhas com Y ímpar
DELETE FROM Q1 WHERE y % 2 <> 0;
DELETE FROM Q2 WHERE y % 2 <> 0;
DELETE FROM Q3 WHERE y % 2 <> 0;
DELETE FROM Q4 WHERE y % 2 <> 0;