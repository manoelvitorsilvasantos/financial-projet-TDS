
from sys import argv
from converter import Converter
from platform import *
from time import sleep

class Main:

	def __init__(self):
		pass
	#converte moedas
	def toCoin(self):
		value = input(' Digite o valor em Real: ')
		moeda = str(input(' Sigla da moeda em questão: '))
		moeda = moeda.upper()
		c = Converter(float(value), moeda.upper())
		saida = c.fromNewCoin()
		print(f'\n\n{value} Reais em {moeda} = {saida}')
		btn = input('\n\nDigite alguma tecla pra voltar\n')
		#verifica se o sistema é linux ou windows
		if system() == 'Linux':
			sys('cls')
		elif system() == 'Window':
			sys('clear')
	#inicio do programa
	def init(self):
		print(
			'--------- MENU DE OPÇÕES ---------------------\n'
			'1 - Planejamento de Receita e despesas\n',
			'2 - Cadastro de Receitas e Despesas realizadas\n',
			'3 - Visualização comparativa\n',
			'4 - Visualização de Saldo\n',
			'5 - Análise de Viabilidade de Investimento\n',
			'6 - Conversão de Moedas\n',
			'0 - Fechar aplicativo\n'
		)
		opc = int(input(' digite um valor correspondente a opção >>  '))

		if (opc == 0):
			print(' Fechando programa...')
			sleep(1)
			exit(0)
		elif (opc == 1):
			plainning()
		elif (opc == 2):
			register()
		elif (opc == 3):
			viewComparative()
		elif (opc == 4):
			viewBalance()
		elif (opc == 5):
			analyseViability()
		elif (opc == 6):
			self.toCoin()
		else:
			print(' Opção Inválida!!!\n')

#roda o programa em um loop infinito
while True:
	Main().init()