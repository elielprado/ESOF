# -*- coding: utf-8 -*-
from DataBase import *
from Professor import *
from Aluno import *

class Cadastro:
    def cadastrarAluno(self, nome, senha, escola, professor):
        print('cadastrando aluno')
        aluno = Aluno(nome, senha, escola, professor)
        try:
            inserirAluno(aluno)
        except:
            print('erro ao cadastrar aluno!')
            createDb()
            inserirAluno(aluno)
        else:
            print('cadastrado com sucesso!')

    def cadastrarProf(self, nome, senha, escola, email):
        print('cadastrando professor')
        professor = Professor(nome, senha, escola, email)
        try:
           inserirProf(professor)
        except:
            print('erro ao cadastrar professor!')
        else:
            print('cadastrado com sucesso!')
