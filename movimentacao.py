import re
import datetime as dt
from firebase import firebase_app

db_movimentacao = firebase_app.getDatabase('/movimentacao')

movimentacao = {
  "valor": float,
  "descricao": str,
  "data": dt.datetime
}

def cadastrar():
  movimentacao['valor'] = getValor()
  movimentacao['descricao'] = getDescricao()
  movimentacao['data'] = getData()

  db_movimentacao.push(movimentacao)

def atualizar():
  print("Atualizando...")
  input("Enter para voltar para o menu!")

def remover():
  print("Removendo...")
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