import pandas as pd
from os import*



#calcular TIR
def tir(valores, datas):
    return newton(lambda taxa:vlp(taxa, valores, datas), 0)

#limpar tela
def limparTela():
    system('cls' if name == 'nt' else 'clear')
def main(cabecalho):
    j = 5#int(input('Periodo em anos >> '))
    rate = 0.05 #float(input('taxa >> '))
    vi = -3000 #float(input('Investimento inicial >> '))
    v1 = 1000 #float(input('valor do primeiro periodo[mes ou ano] >> '))

    total = 0
    flx = list()
    ano = list()
    total_descontado = list()
    saldo = list()


    for i in range(j):
        if i == 0:
            flx.append( vi / (1 + rate) ** i)
            ano.append(i)
            total_descontado.append(-vi)
            saldo.append(round(-(vi) - (v1 / (1 + rate ) ** i), 2))
        elif i == 4:
            flx.append(round((v1 / (1 + rate ) ** i), 2))
            ano.append(i)
            total_descontado.append(v1)
        else:
            flx.append(round((v1 / (1 + rate ) ** i), 2))
            ano.append(i)
            total_descontado.append(v1)
            saldo.append(round(-(vi) - (v1 / (1 + rate ) ** i), 2))

    for r in flx:
        total += round(r, 2)

    saldo.append(round(total, 2))

    data = {
        'Ano': ano,
        'Total': total_descontado,
        'Descontado(R$)': flx,
        'Saldo':saldo
    }

    valores = pd.DataFrame(data)
    print(valores)
