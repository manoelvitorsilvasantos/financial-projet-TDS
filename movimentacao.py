import re
import pandas as pd
import datetime as dt
from firebase import firebase_app
import utils

db = firebase_app.getDatabase('/')

movimentacao = {
  "valor": float,
  "descricao": str,
  "data": dt.datetime
}

def cadastrar(caminho_db):
  movimentacao['valor'] = getValor()
  movimentacao['descricao'] = getDescricao()
  movimentacao['data'] = getData()

  db.child(caminho_db).push(movimentacao)

def atualizar(caminho_db):
  utils.limparTela()
  print('------Atualizando------')
  movimentacoes = db.child(caminho_db).get()
  print(converter(movimentacoes))
  
  idx = int(input("Informe o index da linha que deseja atualizar: "))

  item = converter(movimentacoes, True).iloc[idx]

  utils.limparTela()
  print('......Alterando......')
  print(pd.DataFrame(item))
  print('........Novos valores........')
  movimentacao_atualizada = movimentacao
  movimentacao_atualizada['valor'] = getValor()
  movimentacao_atualizada['descricao'] = getDescricao()
  movimentacao_atualizada['data'] = getData()
  
  db.child(caminho_db).child(item['id']).set(movimentacao_atualizada)

  print("Atualizado com sucesso!")
  input("Enter para voltar para o menu:")


def remover(caminho_db):
  utils.limparTela()
  print('------Removendo------')
  movimentacoes = db.child(caminho_db).get()
  print(converter(movimentacoes))
  
  idx = int(input("Informe o index da linha que deseja Remover: "))

  item = converter(movimentacoes, True).iloc[idx]

  utils.limparTela()
  print('......Removendo......')
  print(pd.DataFrame(item))
  x = input('Tem certeza que deseja deletar esse registro? s ou n: ')

  if x == 's':
    db.child(caminho_db).child(item['id']).delete()
    print('Deletado com sucesso!')
  else: 
    print('Cancelado!')
  input("Enter para voltar para o menu!")

def listar(caminho_db, pausar=True):
  movimentacoes = db.child(caminho_db).get()
  print("_____________________________________")
  print(converter(movimentacoes))
  
  if pausar: input("Enter para voltar para o menu!")

def converter(dados, com_id=False):
  df = pd.DataFrame(
    dados.values(),
    index=range(len(dados)),
  )
  df['data'] = pd.to_datetime(df['data'], format='%d-%m-%Y')

  if com_id:
    df['id'] = dados.keys()
  
  return df

def getValor():
  x = input('Informe o valor: ')

  if(not x):  return getValor()

  if(not x.strip('-').isnumeric()): return getValor()

  return float(x)

def getDescricao():
  desc = input('Informe uma descrição: ')
  if not desc:
    print('Descrição inválida')
    return getDescricao()
  
  return desc

def getData():

  test = "^[0-9]{1,2}\-[0-9]{1,2}\-[0-9]{4}$"
  data_ = input('Infome a data (dd-mm-aaaa): ').strip()
  
  if not re.search(test, data_):
    print('Data inválida!')
    return getData()

  return data_
  # return dt.datetime.strptime(data_, '%d-%m-%Y')