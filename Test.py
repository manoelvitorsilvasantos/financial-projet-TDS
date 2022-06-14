from converter import Converter

value = input('Digite o valor em Real: ')
moeda = str(input('Sigla da moeda em questão: '))
moeda = moeda.upper()
c = Converter(float(value), moeda.upper())
saida = c.fromNewCoin()
print(f'{value} Reais em {moeda} = {saida}')
