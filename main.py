
from sys import argv
from converter import Converter

class Main:

	def __init__(self):
		pass
	def toCoin(self):
		value = input('Digite o valor em Real: ')
		moeda = str(input('Sigla da moeda em questão: '))
		moeda = moeda.upper()
		c = Converter(float(value), moeda.upper())
		saida = c.fromNewCoin()
		print(f'{value} Reais em {moeda} = {saida}')
		btn = input('\n\nDigite alguma tecla pra voltar\n')
	def init(self):
		print(
			'--------- MENU DE OPÇÕES ------------------------\n'
			'1 - Planejamento de Receita e despesas\n',
			'2 - Cadastro de Receitas e Despesas realizadas\n',
			'3 - Visualização comparativa\n',
			'4 - Visualização de Saldo\n',
			'5 - Análise de Viabilidade de Investimento\n',
			'6 - Conversão de Moedas\n'
		)
		opc = int(input(' digite um valor correspondente a opção >>  '))

		if (opc == 1):
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
			print('Opção Inválida!!!\n')

while True:
	Main().init()