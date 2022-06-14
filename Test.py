from converter import Converter

valor = input("Valor da Moeda em questão >> ")
inCoin = str(input("De >> ")).upper()
outCoin = str(input("Para >> ")).upper()

c = Converter(float(valor), inCoin, outCoin).fromNewCoin()
print(f'{valor} {inCoin} para {outCoin} = {c}')
