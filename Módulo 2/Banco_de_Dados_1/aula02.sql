select * from medicos

select * from pacientes
where doença = 'Asma'

SELECT * FROM pacientes
where sexo = 'M'

--INSERT
INSERT INTO Medicos VALUES 
	(9, '27409848921', 'Dr.Bob', 60, 'Rio de Janeiro', 'Clínico', null) 

SELECT * FROM Medicos
--UPDATE
UPDATE Medicos SET idade=59 WHERE codm=9

--DELETE
DELETE FROM Medicos
WHERE codm=9

DELETE FROM Consultas Where idConsulta=1

SELECT * FROM Consultas