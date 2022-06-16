
from sys import argv
from converter import Converter
from platform import *
from time import sleep

class Main:

	def __init__(self):
		pass

	def limpar(self):
		#verifica se o sistema é linux ou windows
		if system() == 'Linux':
			sys('cls')
		elif system() == 'Window':
			sys('clear')
	#converte moedas
	def toCoin(self):
		value = input(' Digite o valor em Real: ')
		moeda = str(input(' Sigla da moeda em questão: '))
		moeda = moeda.upper()
		c = Converter(float(value), moeda.upper())
		saida = c.fromNewCoin()
		print(f'\n\n{value} Reais em {moeda} = {saida}')
		btn = input('\n\nDigite alguma tecla pra voltar\n')
		self.limpar()
	#inicio do programa
	def init(self):
		lista_opcoes = [
			'================= Menu de opções ================',
			'| 1 - Planejamento de Receita e despesas         |',
			'| 2 - Cadastro de Receitas e Despesas realizadas |',
			'| 3 - Visualização comparativa                   |',
			'| 4 - Visualização de Saldo                      |',
			'| 5 - Análise de Viabilidade de Investimento     |',
			'| 6 - Conversão de Moedas                        |',
			'| 0 - Fechar aplicativo                          |',
			'=================================================|',
		]

		for item in lista_opcoes:
			print(item)

		opc = input('| digite um valor correspondente a opção >>  ')

		if opc.isdigit() == True:
			self.limpar()

			opc = int(opc)

			if (opc == 0):
				print(' Fechando programa...')
				sleep(1)
				exit(0)
			#elif (opc == 1):
				#plainning()
			#elif (opc == 2):
				#register()
			#elif (opc == 3):
				#viewComparative()
			#elif (opc == 4):
				#viewBalance()
			#elif (opc == 5):
				#analyseViability()
			elif (opc == 6):
				self.toCoin()
			else:
				print(' Opção Inválida!!!\n')
		else:
			print('Error, Você precisa digitar um valor númerico!!!')
#roda o programa em um loop infinito
while True:
	c = Main()
	c.init()