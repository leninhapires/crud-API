-- Active: 1727434778550@@localhost@5432@AlunoDB
SELECT * FROM "Alunos";


INSERT INTO "Alunos"(nome,email)
VALUES
    ('mary','mary@email.com'),
    ('joana','joana@email.dot'),
    ('alan','alan@teste.com')

DELETE FROM public."Alunos"
WHERE nome = ''

