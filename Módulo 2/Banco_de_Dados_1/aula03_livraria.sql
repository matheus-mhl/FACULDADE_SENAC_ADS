-- CRIANDO UMA NOVA LIVRARIA
-- DDL: Criação das tabelas
CREATE TABLE Professores (
    id_professor INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    data_contratacao DATE NOT NULL,
    departamento VARCHAR(50) NOT NULL
);

CREATE TABLE Disciplinas (
    codigo_disciplina VARCHAR(6) PRIMARY KEY,
    nome_disciplina VARCHAR(100) NOT NULL,
    creditos INT NOT NULL CHECK (creditos > 0)
);

CREATE TABLE Estudantes (
    id_estudante INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL
);

CREATE TABLE Turmas (
    id_turma INT PRIMARY KEY,
    codigo_disciplina VARCHAR(6) NOT NULL,
    id_professor INT NOT NULL,
    semestre VARCHAR(10) NOT NULL,
    ano INT NOT NULL,
    FOREIGN KEY (codigo_disciplina) REFERENCES Disciplinas(codigo_disciplina),
    FOREIGN KEY (id_professor) REFERENCES Professores(id_professor)
);

CREATE TABLE Matriculas (
    id_matricula INT PRIMARY KEY,
    id_estudante INT NOT NULL,
    id_turma INT NOT NULL,
    data_matricula DATE NOT NULL DEFAULT GETDATE(),
    UNIQUE (id_estudante, id_turma),
    FOREIGN KEY (id_estudante) REFERENCES Estudantes(id_estudante),
    FOREIGN KEY (id_turma) REFERENCES Turmas(id_turma)
);

CREATE TABLE Pre_requisitos (
    disciplina_principal VARCHAR(6) NOT NULL,
    disciplina_requisito VARCHAR(6) NOT NULL,
    PRIMARY KEY (disciplina_principal, disciplina_requisito),
    FOREIGN KEY (disciplina_principal) REFERENCES Disciplinas(codigo_disciplina),
    FOREIGN KEY (disciplina_requisito) REFERENCES Disciplinas(codigo_disciplina)
);


INSERT INTO Professores (id_professor, nome, data_contratacao, departamento) VALUES
(201, 'Fernando', '2010-08-01', 'Ciência da Computação'),
(202, 'Helena', '2015-03-10', 'Matemática'),
(203, 'João', '2018-05-20', 'Física'),
(204, 'Michael', '2020-02-15', 'Ciência da Computação'),
(208, 'Roberto', '2019-01-01', 'Biologia'),
(209, 'Mariana', '2022-04-10', 'Engenharia');


INSERT INTO Disciplinas (codigo_disciplina, nome_disciplina, creditos) VALUES
('ENG001', 'Engenharia de Software', 6),
('MAT101', 'Cálculo I', 4),
('FIS201', 'Física Moderna', 5),
('ART301', 'Desenho Artístico', 7),
('ENG451', 'Engenharia de Software', 4),
('FIS251', 'Física Geral', 3),
('MAT121', 'Matemática Aplicada', 4),
('BIO599', 'Biologia Marinha', 5),
('CDC512', 'Ciências da Computação', 4),
('MAT873', 'Matemática', 9);


INSERT INTO Estudantes (id_estudante, nome, email, data_nascimento) VALUES
(101, 'Ana', 'ana.souza@email.com', '2001-05-15'),
(102, 'Bruno', 'bruno.silva@email.com', '2000-11-20'),
(103, 'Carla', 'carla.santos@email.com', '2002-03-10'),
(104, 'Daniela', 'ana.souzaa@email.com', '2003-09-25');


INSERT INTO Turmas (id_turma, codigo_disciplina, id_professor, ano, semestre) VALUES
(1, 'ENG451', 201, 2023, '1º'),
(2, 'MAT121', 202, 2023, '1º'),
(3, 'FIS251', 203, 2023, '2º'),
(4, 'BIO599', 208, 2023, '2º'),
(5, 'ENG451', 209, 2023, '2º'),
(6, 'CDC512', 201, 2023, '1º');


SELECT * FROM Estudantes;
SELECT * FROM Disciplinas;
SELECT * FROM Professores;
SELECT * FROM Turmas;