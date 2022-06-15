
from sys import arv
from menu import Menu
from converter import Converter

class Main:

	def __init__(self):
		pass
	def init():
		opc = int(argv(1))
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
			converterCoin()
	def toCoin()
		value = input('Digite o valor em Real: ')
		moeda = str(input('Sigla da moeda em questão: '))
		moeda = moeda.upper()
		c = Converter(float(value), moeda.upper())
		saida = c.fromNewCoin()
		print(f'{value} Reais em {moeda} = {saida}')

