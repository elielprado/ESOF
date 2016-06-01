class cadastro:
	nome='Eliel'
	escola='UFU'
	email='eliel.resende@hotmail.com'
	senha='elielprado'
	def cadastrarAluno()
	
class professor:
	nome=cadastro.nome
	escola=cadastro.escola
	senha=cadastro.senha
	def cadastrarProfessor()
	def fazerLogin()
	def criarAulas()
	def criarExercicios()
	def acompanharDesempenho()
class aluno:
	nome=cadastro.nome
	escola=cadastro.escola
	professor=professor.nome
	senha=cadastro.senha
	def fazerLogin()
	def fazerAula()
	def fazerExercicios()
class desempenho:
	frequencia=25
	notas=60
class login:
	nome=cadastro.nome
	senha=cadastro.senha
print "Bem vindo"
dir(aluno)
dir(desempenho)
dir(cadastro)
dir(login)
dir(professor)
