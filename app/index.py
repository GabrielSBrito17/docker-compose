import sys
import main
import pandas as pd


while True:
  owner = str(input("Nome do proprietário: "))
  people = main.filter_db(f"{owner}")
  if people.name.empty is True:
    register_person = owner
  else:
    cars = int(input("Possui quantos carros?: "))
    qtd_cars = main.filter_db(f"{cars}")
    include_people = main.insert_db(f"{i}", f"{owner}", qtd_cars=None, models=None, colors=None)
    colors = str(input("Qual dessas cores de carro deseja?(Amarelo, Azul, Cinza): "))
    models = str(input("Qual desses modelos de carro deseja?(Hatch, Sedan, Conversível): "))
    people = main.filter_db(f"{owner}")
  if people is True:
    reg = main.filter_db(f"{owner}")
    print(reg)
  if cars == 3:
    print("O Sr(a). já possui 3 carros.")
    sale = str(input("Deseja vender algum de seus carros? Yes/No")).upper()
    if sale == ('yes').upper():
      main.update_db(sale, people.id[0])

  else:
    sql_cars = f"INSERT into cars (id, colors, models, owner_id) value ('1', '{colors}', '{models}', '1' )"
    main.insert_db()

