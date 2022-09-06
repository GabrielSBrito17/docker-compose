from app.models.owner import Owner
# from tinydb import TinyDB, Query
import pandas as pd
import app.main as main

def inserir(model: Owner):
  main.insert_db(model.id, model.name, model.qtd_cars, model.models, model.colors)

def mostrarTodos():
  todos = main.consult_db("owners")
  return todos

def deletarPessoa(name: str, model: Owner):
  if main.filter_db(model.name == str(name)):
    main.delete_db(model.name == str(name))
  else:
    print("Usuário não encontrado")

def atualizarPessoa(name: str, model: Owner):
  if main.filter_db(model.name == str(name)):
    main.delete_db(model.name == str(name))
    inserir(model)
  else:
    print("Esse usuário não existe")


def mostrarTabelaTodos():
  todos = pd.DataFrame(main.consult_db("owners"))
  return todos.to_json()


def search_for_name(name):
  owners = Owner()
  return main.consult_db(owners.name == str(name))


def count():
  total_cadastrado = len(main.consult_db("owners"))
  return total_cadastrado