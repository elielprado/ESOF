# -*- coding: utf-8 -*-
import sqlite3

connection = sqlite3.connect('database.db')
connect = connection.cursor()
logged = 0
user_name = ''
connection.text_factory = str
def cls():
    print "\n" * 100

def createDb():
    connect.execute('CREATE TABLE alunos(nome text, senha text, escola text, professor text);')

def inserirAluno(aluno):
    connect.execute('INSERT INTO alunos VALUES(?,?,?,?)', (aluno.nome, aluno.senha, aluno.escola, aluno.professor))
    connection.commit()
def inserirProf(professor):
    connect.execute('INSERT INTO professores VALUES(?,?,?,?)', (professor.nome, professor.senha, professor.escola, professor.email))
    connection.commit()
def inserirAula(professor, tituloAula, conteudo):
    connect.execute('INSERT INTO aulas VALUES(?,?,?)', (professor, tituloAula, conteudo))
    connection.commit()
def inserirExercicios(professor, tituloExercicios, conteudo):
    connect.execute('INSERT INTO exercicios VALUES(?,?,?)', (professor, tituloExercicios, conteudo))
    connection.commit()
def inserirResolucaoExercicios(nome, professor, titulo, conteudo):
    connect.execute('INSERT INTO resolucaoExercicios VALUES(?,?,?,?)', (nome, professor, titulo, conteudo))
    connection.commit()
def avaliarAluno(nome, professor, frequencia, nota):
    connect.execute('INSERT INTO desempenho VALUES(?,?,?,?)', (nome, professor, frequencia, nota))
    connection.commit()
def getDesempenho(nome):
    connect.execute('SELECT * FROM desempenho WHERE nome="%s"' % (nome))
    rows = connect.fetchall()
    desempenho = []
    if rows is not None:
        for row in rows:
            if row is None:
                break
            else:
                desempenho.append(row)
    else:
        print('O professor ainda nao o avaliou, ' + nome + '!')
    return desempenho
def getAula(professor):
    aulas = []
    connect.execute('SELECT * FROM aulas WHERE professor="%s"' % (professor))
    rows = connect.fetchall()
    if rows is not None:
        for row in rows:
            if row is None:
                break
            else:
                print(row)
                aulas.append(row)
    else:
        print('O professor ainda nao enviou nenhuma aula!')
    return aulas
def getAlunos(professor):
    alunos = []
    connect.execute('SELECT * FROM alunos WHERE professor="%s"' % (professor))
    rows = connect.fetchall()
    if rows is not None:
        for row in rows:
            if row is None:
                break
            else:
                alunos.append(row)
    else:
        print('Voce ainda nao possui nenhum aluno cadastrado!')
    return alunos
def getExercicios(professor):
    exercicios = []
    connect.execute('SELECT * FROM exercicios WHERE professor="%s"' % (professor))
    rows = connect.fetchall()
    if rows is not None:
        for row in rows:
            if row is None:
                break
            else:
                exercicios.append(row)
    else:
        print('O professor ainda não enviou exercicios!')
    return exercicios
def getExerciciosResolvidos(professor):
    exercicios = []
    connect.execute('SELECT * FROM resolucaoExercicios WHERE professor="%s"' % (professor))
    rows = connect.fetchall()
    if rows is not None:
        for row in rows:
            if row is None:
                break
            else:
                exercicios.append(row)
    else:
        print('Nenhum exercicio foi resolvido ainda pelos alunos.')
    return exercicios