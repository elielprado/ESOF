# -*- coding: utf-8 -*-
from DataBase import *

class Professor:
    def __init__(self, nome, senha, escola, email):
        self.nome = nome
        self.escola = escola
        self.senha = senha
        self.email = email

    def criarAula(self):
        print('\n' * 2)
        print('Importante!: Na ultima linha para indicar que o texto ja foi adicionado, coloque o operador /end!')
        titulo = raw_input('Informe o titulo da aula: ')
        print('Informe o conteudo da aula (Permitido texto e links): \n')
        lines = []
        while True:
            line = raw_input()
            if line == '/end':
                break
            else:
                if line:
                    lines.append(line + '\n')

        text = ''.join(lines)
        try:
            inserirAula(self.nome, titulo, text)
        except:
            print('Erro ao adicionar aula')
        else:
            print('\nAula adicionada com sucesso!')
    def criarExercicios(self):
        print('\n' * 2)
        print('Importante!: Na ultima linha para indicar que o texto ja foi adicionado, coloque o operador /end!')
        titulo = str(raw_input('Informe o titulo dos exercicios: '))
        print('Informe o conteudo dos exercicios (Permitido texto e links): \n')
        lines = []
        while True:
            line = str(raw_input())
            if line == '/end':
                break
            else:
                if line:
                    lines.append(line + '\n')

        text = ''.join(lines)

        print('\n')
        try:
            inserirExercicios(self.nome, titulo, text)
        except:
            print('Erro ao adicionar exercicios')
        else:
            print('\nExercicios adicionados com sucesso!')

    def acompanharDesempenho(self):
        while True:
            print('\n *** Area avaliativa ***\n')
            print('O que deseja fazer? ')
            print('1- Ver exercicios resolvidos')
            print('2- Avaliar aluno')
            print('3- Sair')
            opt = int(raw_input('Informe o numero da opção '))
            if opt == 1:
                print('\nEscolha o aluno/exercicio para ver sua resolução\n')
                exercicios = getExerciciosResolvidos(self.nome)
                i = 0
                for exercicio in exercicios:
                    print(str(i + 1) + ' - ' + exercicio[0] + ' : ' + exercicio[2])
                    i += 1
                exIndex = int(raw_input('Informe o numero da opção '))
                exercicio = exercicios[exIndex - 1]
                print('\nMostrando resolução do exercicio ' + exercicio[2] + ' feito por ' + exercicio[0])
                print('\n')
                print(exercicio[3])
            elif opt == 2:
                print('\nEscolha o aluno a ser avaliado: ')
                alunos = getAlunos(self.nome)
                i = 0
                for aluno in alunos:
                    print(str(i + 1) + ' - ' + aluno[0])
                    i += 1
                alunoIndex = int(raw_input('Informe o numero da opção '))
                aluno = alunos[alunoIndex - 1]
                nota = int(raw_input('Informe a nota do aluno: '))
                frequencia = int(raw_input('Informe a frequencia do aluno: '))
                try:
                    avaliarAluno(aluno[0], self.nome, frequencia, nota)
                except:
                    print('\nFalha ao avaliar aluno, tente novamente mais tarde.')
                else:
                    print('\nAluno avaliado com sucesso!')
            else:
                break