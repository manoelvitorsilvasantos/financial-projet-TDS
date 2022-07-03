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
  print("Cadastrado com sucesso!")
  input("Enter para voltar para o menu:")

def atualizar(caminho_db):
  utils.limparTela()
  print('------Atualizando------')
  movimentacoes = db.child(caminho_db).get()
  df_movimentacoes = converter(movimentacoes, True)
  print(df_movimentacoes.drop(columns=["id"]))
  
  idx = int(input("Informe o index da linha que deseja atualizar: "))

  item = df_movimentacoes.iloc[idx]

  utils.limparTela()
  print('......Alterando......')
  print(item.drop(labels=['id']).to_string())
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
  df_movimentacoes = converter(movimentacoes, True)
  print(df_movimentacoes.drop(columns=["id"]))
  
  idx = int(input("Informe o index da linha que deseja Remover: "))

  item = df_movimentacoes.iloc[idx]

  utils.limparTela()
  print('......Removendo......')
  print(item.drop(labels=['id']).to_string())
  x = input('Tem certeza que deseja deletar esse registro? s ou n: ')

  if x == 's':
    db.child(caminho_db).child(item['id']).delete()
    print('Deletado com sucesso!')
  else: 
    print('Cancelado!')
  input("Enter para voltar para o menu!")

def buscar_todos(caminho_db):
  return db.child(caminho_db).get()

def listar(caminho_db, pausar=True):
  movimentacoes = buscar_todos(caminho_db)
  print("_____________________________________")
  print(converter(movimentacoes).sort_values(['data']))
  
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

def mostrar_saldo():
  utils.limparTela()

  movs = buscar_todos('fluxo')

  df = pd.DataFrame(movs.values())
  df['data'] = pd.to_datetime(df['data'], format='%d-%m-%Y')
  df.set_index('data', inplace=True)
  df.sort_index(inplace=True)
  df['total'] = df['valor'].cumsum()

  print(df)
  print("________________________________________")
  print("::::::::::::::: SALDO ::::::::::::::::::")
  print(df['total'].tail(1).to_string())
  input("Enter para voltar para o menu!")


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