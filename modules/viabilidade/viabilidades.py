import pandas as pd
from os import*


#CALCULAR VALOR VALOR LIQUIDO
def vlp(taxa, valores, datas):
    data_minima = min(datas)
    return sum([
        valores/(1 + taxa)**((data - data_minima).days/365)
        for valor, data
        in zip(valores, datas)
    ])

#calcular TIR
def tir(valores, datas):
    return newton(lambda taxa:vlp(taxa, valores, datas), 0)

#limpar tela
def limparTela():
    system('cls' if name == 'nt' else 'clear')

def fluxo_meses():
    lista_meses = list()
    lista_valores = list()
    
    meses = int(input('Em quantos meses: ')) + 1
    taxa = float(input('Valor da taxa p/ ano {valor inteiro}: '))
def fluxo_anos():
    anos = int(input('Em quantos anos: ')) + 1
def main(cabecalho):
    limparTela()
    periodo = list()
    valores = list()
    print(':::::::::::::|{}|:::::::::::::'.format(cabecalho))
    escolha = input('Análise de fluxo em [1] meses ou [2] anos?')

    if escolha == 1:
        fluxo_meses()
    elif escolha == 2:
        fluxo_anos()



main('Análise de Viabilidade de investimento')
