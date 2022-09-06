# import sys
# import main
# import pandas as pd
#
# owner = str(input("Nome do proprietário: "))
# cars = int(input("Possui quantos carros?: "))
# colors = str(input("Qual dessas cores de carro deseja?(Amarelo, Azul, Cinza): "))
# models = str(input("Qual desses modelos de carro deseja?(Hatch, Sedan, Conversível): "))
#
#
#
# if cars == 3:
#   print("O Sr(a). já possui 3 carros.")
# else:
#   sql_cars = f"INSERT into cars (id, colors, models, owner_id) value ('1', '{colors}', '{models}', '1' )"
#   main.insert_db(sql_cars)

from src.model import Pessoa
# from tinydb import TinyDB, Query
import pandas as pd
import main

# bd = TinyDB("Pessoas.json")
# usuario = Query()


def inserir(model: Pessoa):
  '''Insere um modelo no banco de dados'''

  main.insert_db(model.id, model.name, model.qtd_cars, model.models_cars, model.colors_cars)
  # bd.insert({"CPF": model.CPF,
  #            "Nome": model.nome,
  #            "DataNascimento": model.dataNascimento})


def mostrarTodos():
  '''Mostra todos os contatos cadastrados no banco de dados'''

  todos = main.consult_db("owner")
  return todos


def deletarPessoa(cpf: int):
  '''Busca um CPF e deleta o registro do modelo encontrado'''
  if bd.search(usuario.CPF == str(cpf)):
    bd.remove(usuario.CPF == str(cpf))
  else:
    print("Usuário não encontrado")


def atualizarPessoa(cpf: int, model: Pessoa):
  """Atualiza um modelo no banco de dados"""
  if bd.search(usuario.CPF == str(cpf)):
    bd.remove(usuario.CPF == str(cpf))
    inserir(model)
  else:
    print("Esse usuário não existe")


def mostrarTabelaTodos():
  todos = pd.DataFrame(bd)
  return todos.to_html()


def buscarPorCPF(cpf):
  return bd.search(usuario.CPF == str(cpf))


def count():
  total_cadastrado = len(bd.all())
  return total_cadastrado