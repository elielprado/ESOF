# -*- coding: utf-8 -*-
from DataBase import *
from Professor import *
from Aluno import *
from Cadastro import *

class Login:
    def logInAluno(self, username, senha):
        connect.execute('SELECT * FROM alunos WHERE nome="%s" AND senha="%s"' % (username, senha))
        row = connect.fetchone()
        if row is not None:
            print('\n *** Seja bem vindo ' + username + ' ***')
            global logged
            logged = 1
            aNome = row[0]
            aEscola = row[2]
            pNome = row[3]
            aluno = Aluno(aNome, senha, aEscola, pNome)
            while True:
                print('\nO que deseja fazer?\n')
                print('1- Ver aulas')
                print('2- Fazer exercicios')
                print('3- Acompanhar desempenho')
                print('4- Sair (logout)')
                opt = int(raw_input('Digite o numero da opção '))
                if opt == 1:
                    aluno.fazerAula()
                elif opt == 2:
                    aluno.fazerExercicios()
                elif opt == 3:
                    aluno.acompanharDesempenho()
                elif opt == 4:
                    break
        else:
            print('Falha ao logar. User ou senha incorretos!')
            global logged
            logged = 0

    def logInProfessor(self, email, senha):
        connect.execute('SELECT * FROM professores WHERE email="%s" AND senha="%s"' % (email, senha))
        row = connect.fetchone()
        if row is not None:
            global logged
            logged = 1
            pName = row[0]
            pEscola = row[2]
            prof = Professor(pName, senha, pEscola, email)
            while True:
                print('\n')
                print(pEscola + ' - Seja bem vindo, ' + pName + '!\n')
                print('O que deseja fazer? ')
                print('\n')
                print('1- Criar aula')
                print('2- Criar exercicios')
                print('3- Acompanhar desempenho')
                print('4- Cadastrar aluno')
                print('5- Cadastrar outro professor')
                print('6- Sair (logout).')
                opt = int(raw_input('Informe o numero da opção '))
                if opt == 1:
                    prof.criarAula()
                elif opt == 2:
                    prof.criarExercicios()
                elif opt == 3:
                    prof.acompanharDesempenho()
                elif opt == 4:
                    cad = Cadastro()
                    username = raw_input('User: ')
                    senha = raw_input('Senha: ')
                    cad.cadastrarAluno(username, senha, pEscola, pName)
                elif opt == 5:
                    print('\nCadastrar professor:\n')
                    username = raw_input('nome: ')
                    senha = raw_input('senha: ')
                    email = raw_input('email: ')
                    escola = raw_input('escola: ')
                    cad = Cadastro()
                    cad.cadastrarProf(username, senha, escola, email)
                else:
                    break
        else:
            print('Falha ao logar. User ou senha incorretos!')