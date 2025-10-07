CREATE TABLE TIMES(Abreviacao VARCHAR(3) PRIMARY KEY NOT NULL,
Nome VARCHAR(100),
Estado VARCHAR(2)
);

SELECT * FROM TIMES;

INSERT INTO TIMES(Abreviacao, Nome, Estado)
VALUES('FLA', 'Flamengo', 'RJ'),
('VAS', 'Vasco', 'RJ'),
('FLU', 'Fluminense', 'RJ'), 
('BOT', 'Botafogo', 'RJ'), 
('AFC', 'América', 'RJ'),
('SCC', 'Corinthians', 'SP'),
('GFC', 'Guarani', 'SP'),
('CAM', 'Atlético Mineiro', 'MG');

CREATE TABLE JOGADORES(ID VARCHAR(100) PRIMARY KEY NOT NULL,
Nome VARCHAR(100),
Posicao VARCHAR(100),
Equipe VARCHAR(3)
);

SELECT * FROM JOGADORES;

INSERT INTO JOGADORES(ID, Nome, Posicao, Equipe)
VALUES( '12345678901', 'Coutinho', 'Atacante', 'VAS' ),
( '12345678911', 'Payet', 'Meio Campo', 'VAS' ),
( '12345678111', 'Bruno Henrique', 'Ponta Esquerda', 'FLA' ),
( '12345671111', 'Gonzalo Plata', NULL, 'FLA' ),
( '02345678911', 'GANSO', 'Meio Campo', 'FLU' ),
( '00345678911', 'Romario', 'Atacante', 'AFC' ),
( '00045678911', 'Josue', 'Atacante', 'CAM' ),
( '00044478911', 'Emerson', 'Goleiro', 'GFC' ),
( '00055578911', 'Emerson', 'Zagueiro', 'SCC' ),
( '00055578912', 'Patrick', 'Meia', 'BOT' );

SELECT * FROM JOGADORES;

/*CAMPEONATO
(001, 'Brasileirão'), 
(002, 'Copa do Brasil'),
(003, 'Libertadores'), 
(004, 'Carioca'), 
(005, 'Paulistão')
(006, 'Mineiro')*/

/*
PARTICIPACAO
 - Flamengo participa no Carioca, Brasileirão, Copa do Brasil e Libertadores;
 - Vasco participa no  Carioca, Brasileirão e Copa do Brasil;
 - Fluminense participa no Carioca, Brasileirão e Libertadores
 - Guarani participa no Paulistao e Brasileirão
 - Corinthians participa no Paulistão, Brasileirão e Libertadores
 - Botafogo participa no  Carioca, Brasileirão e Copa do Brasil;
 - América participa no  Carioca;
 - Atlético Mineiro participa no  Mineiro, Brasileirão e Copa do Brasil

*/





