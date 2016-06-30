from Professor import *
from Aluno import *
from Login import *
from Cadastro import *

def init():
    global logged
    
    while True:
        if logged == 0:
            print('Seja bem vindo!')

        opt2 = int(raw_input('\nDigite 1 para logar como *aluno ou 2 para logar como *professor: '))
        username = ''
        senha = ''
        email = ''

        if opt2 == 2:
            print('\nOla professor, entre com seus dados')
            email = raw_input('Email: ')
            senha = raw_input('Senha: ')
            login = Login()
            login.logInProfessor(email, senha)
        elif opt2 == 1:
            print('\nCaro aluno, entre com seus dados')
            username = raw_input('User: ')
            senha = raw_input('Senha: ')
            login = Login()
            login.logInAluno(username, senha)
init()

