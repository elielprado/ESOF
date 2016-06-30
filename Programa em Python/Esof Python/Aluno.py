# -*- coding: utf-8 -*-
from DataBase import *

class Aluno:
    def __init__(self, nome, senha, escola, professor):
        self.nome = nome
        self.senha = senha
        self.escola = escola
        self.professor = professor
    def fazerAula(self):
        aulas = getAula(self.professor)
        i = 0
        for aula in aulas:
            id = i + 1
            print(str(id) + ' - ' + aula[1])
            i += 1
        aulaOpt = int(raw_input('Escolha a aula que você deseja ver: '))
        aula = aulas[aulaOpt - 1]
        print('\n')
        print(' *** ' + aula[1] + ' ***\n')
        print(aula[2])

    def fazerExercicios(self):
        exercicios = getExercicios(self.professor)
        i = 0
        for exercicio in exercicios:
            id = i + 1
            print(str(id) + ' - ' + exercicio[1])
            i += 1
        exercOpt = int(raw_input('Escolha o exercicio para fazer: '))
        exercicio = exercicios[exercOpt - 1]
        print('\n')
        print(' *** ' + exercicio[1] + ' ***\n')
        print(exercicio[2])
        print('\n' * 2)
        print('Importante!: Na ultima linha para indicar que o texto ja foi adicionado, coloque o operador /end!')
        print('Informe a resolução do(s) exercicio(s): \n')
        lines = []
        while True:
            line = str(raw_input())
            if line == '/end':
                break
            else:
                if line:
                    lines.append(line + '\n')

        text = ''.join(lines)

        try:
            inserirResolucaoExercicios(self.nome, self.professor, exercicio[1], text)
        except:
            print('Erro ao enviar exercicios')
        else:
            print('\nExercicios enviados com sucesso!\n')
    def acompanharDesempenho(self):
        desempenho = getDesempenho(self.nome)
        if desempenho is not None:
            for x in desempenho:
                print('\nSeu desempenho com o professor ' + x[1] + ':\n' + ' - frequencia: ' + str(x[2]) + '\n' + ' - nota: ' + str(x[3]) + '\n')