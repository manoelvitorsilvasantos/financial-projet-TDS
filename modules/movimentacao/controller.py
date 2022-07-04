from firebase import firebase_app
from firebase_admin.exceptions import FirebaseError

db = firebase_app.getDatabase('/')

movimentacao = {
  "valor": float,
  "descricao": str,
  "data": str
}

def cadastrar(caminho_db, obj: movimentacao):
  try:
    db.child(caminho_db).push(obj)
  except ValueError:
    print("Erro ao acessar o Firebase")
  except FirebaseError:
    print("Erro na conexão com o Firebase")
  else:
    return True

def atualizar(caminho_db: str, new_obj: movimentacao, id: str):
  
  try:
    db.child(caminho_db).child(id).set(new_obj)
  except ValueError:
    print("Erro ao acessar o Firebase")
  except FirebaseError:
    print("Erro na conexão com o Firebase")
  else:
    return True


def remover(caminho_db: str, id: str):

  try:
    db.child(caminho_db).child(id).delete()
  except ValueError:
    print("Erro ao acessar o Firebase")
  except FirebaseError:
    print("Erro na conexão com o Firebase")
  else:
    return True

def buscar_todos(caminho_db):
  try:
    all = db.child(caminho_db).get()
  except ValueError:
    print("Erro ao acessar o Firebase")
  except FirebaseError:
    print("Erro na conexão com o Firebase")
  else:
    return all
  