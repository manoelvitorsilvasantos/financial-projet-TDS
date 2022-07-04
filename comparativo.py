import modules.utils as utils
import pandas as pd
from dateutil.relativedelta import relativedelta
from modules.movimentacao.movimentacao import movimentsDataFrame

def getData():
  utils.limparTela()
  print("\t:::: Planejado X Real ::::")
  print("_________________________________________")
  print("Ano: 2022")
  mes = getMes()

  f = flowOfMonth(mes)

  if f.empty:
    print('Nenhuma movimentação nesse mês')
  else:
    print(f)
  input("Enter para voltar para o menu")

def flowOfMonth(m: int):
  START = pd.to_datetime('{}{}'.format(m, pd.to_datetime('today').year), format='%m%Y')

  END = START + pd.to_timedelta(pd.Timestamp(START).days_in_month -1, unit='day')

  calendar = pd.DataFrame(index=pd.date_range(start=START, end=END, freq='D'))
  
  flow = movimentsDataFrame('fluxo').loc[START:END]
  flow['total'] = flow['valor'].cumsum()

  plan = movimentsDataFrame('planejamento').loc[START:END]
  plan['total'] = plan['valor'].cumsum()

  rules = {'valor': 0, 'total': 0, 'descricao': ''}

  calendar = pd.concat([calendar, flow], axis=1).dropna(how='all').fillna(rules)
  calendar = pd.concat([calendar, plan], axis=1).dropna(how='all').fillna(rules)


  return calendar
  
def getMes():
  mes = input('Informe o mês: ')

  if(not mes):  return getMes()

  if(not mes.isnumeric()): return getMes()

  return int(mes)