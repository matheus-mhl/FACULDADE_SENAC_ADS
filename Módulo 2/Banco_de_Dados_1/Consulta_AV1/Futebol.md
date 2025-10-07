LEMBRETE: os códigos do professor estão disponíveis no moodle

⚽ Entidades e atributos

Time → nome, sigla (única), estado

Jogador → CPF, nome, posição, sigla_time

Campeonato → código, nome

Participação → relaciona Time ↔ Campeonato (pois um time pode jogar em vários campeonatos)

💾 Modelo relacional
1️⃣ Criação das tabelas
-- Tabela de times
CREATE TABLE Time (
    sigla CHAR(3) PRIMARY KEY,        -- Ex: 'FLA'
    nome VARCHAR(50) NOT NULL,        -- Ex: 'Flamengo'
    estado CHAR(2) NOT NULL           -- Ex: 'RJ'
);

-- Tabela de jogadores
CREATE TABLE Jogador (
    cpf CHAR(11) PRIMARY KEY,         -- Ex: '12345678901'
    nome VARCHAR(50) NOT NULL,
    posicao VARCHAR(30),
    sigla_time CHAR(3),               -- FK referenciando o time
    FOREIGN KEY (sigla_time) REFERENCES Time(sigla)
);

-- Tabela de campeonatos
CREATE TABLE Campeonato (
    codigo INT PRIMARY KEY,           -- Ex: 001
    nome VARCHAR(50) NOT NULL
);

-- Tabela de participação (relação N:N entre Time e Campeonato)
CREATE TABLE Participacao (
    sigla_time CHAR(3),
    codigo_campeonato INT,
    PRIMARY KEY (sigla_time, codigo_campeonato),
    FOREIGN KEY (sigla_time) REFERENCES Time(sigla),
    FOREIGN KEY (codigo_campeonato) REFERENCES Campeonato(codigo)
);

2️⃣ Inserção de dados
🏟️ Times
INSERT INTO Time VALUES
('FLA', 'Flamengo', 'RJ'),
('VAS', 'Vasco', 'RJ'),
('FLU', 'Fluminense', 'RJ'),
('BOT', 'Botafogo', 'RJ'),
('AFC', 'América', 'RJ'),
('SCC', 'Corinthians', 'SP'),
('GFC', 'Guarani', 'SP'),
('CAM', 'Atlético Mineiro', 'MG');

👟 Jogadores
INSERT INTO Jogador VALUES
('12345678901', 'Coutinho', 'Atacante', 'VAS'),
('12345678911', 'Payet', 'Meio Campo', 'VAS'),
('12345678111', 'Bruno Henrique', 'Ponta Esquerda', 'FLA'),
('12345671111', 'Gonzalo Plata', NULL, 'FLA'),
('02345678911', 'Ganso', 'Meio Campo', 'FLU'),
('00345678911', 'Romario', 'Atacante', 'AFC'),
('00045678911', 'Josue', 'Atacante', 'CAM'),
('00044478911', 'Emerson', 'Goleiro', 'GFC'),
('00055578911', 'Emerson', 'Zagueiro', 'SCC'),
('00055578911', 'Patrick', 'Meia', 'BOT');


⚠️ Observação: o último INSERT precisa ter CPF diferente para Patrick, pois CPF é PRIMARY KEY.
Então altere para:

('00055578912', 'Patrick', 'Meia', 'BOT');

🏆 Campeonatos
INSERT INTO Campeonato VALUES
(1, 'Brasileirão'),
(2, 'Copa do Brasil'),
(3, 'Libertadores'),
(4, 'Carioca'),
(5, 'Paulista'),
(6, 'Mineiro');

🤝 Participações
-- Flamengo: Carioca, Brasileirão, Copa do Brasil, Libertadores
INSERT INTO Participacao VALUES
('FLA', 4), ('FLA', 1), ('FLA', 2), ('FLA', 3);

-- Vasco: Carioca, Brasileirão, Copa do Brasil
INSERT INTO Participacao VALUES
('VAS', 4), ('VAS', 1), ('VAS', 2);

-- Fluminense: Carioca, Brasileirão, Libertadores
INSERT INTO Participacao VALUES
('FLU', 4), ('FLU', 1), ('FLU', 3);

-- Guarani: Paulista, Brasileirão
INSERT INTO Participacao VALUES
('GFC', 5), ('GFC', 1);

-- Corinthians: Paulista, Brasileirão, Libertadores
INSERT INTO Participacao VALUES
('SCC', 5), ('SCC', 1), ('SCC', 3);

-- Botafogo: Carioca, Brasileirão, Copa do Brasil
INSERT INTO Participacao VALUES
('BOT', 4), ('BOT', 1), ('BOT', 2);

-- América: Carioca
INSERT INTO Participacao VALUES
('AFC', 4);

-- Atlético Mineiro: Mineiro, Brasileirão, Copa do Brasil
INSERT INTO Participacao VALUES
('CAM', 6), ('CAM', 1), ('CAM', 2);

📘 Explicação passo a passo (documentação)
🔹 Etapa 1: Identificação das entidades

Time, Jogador, Campeonato e Participação foram identificadas com base nas regras do enunciado.

Cada uma virou uma tabela.

🔹 Etapa 2: Definição de chaves

sigla → chave primária de Time (única por regra de negócio).

cpf → chave primária de Jogador.

codigo → chave primária de Campeonato.

sigla_time + codigo_campeonato → chave composta em Participacao (porque um time pode estar em vários campeonatos).

🔹 Etapa 3: Definição dos relacionamentos

Time 1:N Jogador → um time tem vários jogadores.

Implementado com FOREIGN KEY (sigla_time) em Jogador.

Time N:N Campeonato → um time pode participar de vários campeonatos.

Implementado pela tabela Participacao.

🔹 Etapa 4: Inserção dos dados

Os INSERTs seguem os dados fornecidos no slide.

A tabela Participacao resolve a relação N:N sem redundância.

🔹 Etapa 5: Consultas de teste
-- Listar times e campeonatos em que participam
SELECT t.nome AS Time, c.nome AS Campeonato
FROM Participacao p
JOIN Time t ON p.sigla_time = t.sigla
JOIN Campeonato c ON p.codigo_campeonato = c.codigo;

-- Listar jogadores de um time específico
SELECT nome, posicao
FROM Jogador
WHERE sigla_time = 'FLA';