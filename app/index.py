import sys
import main
import pandas as pd

owner = str(input("Nome do proprietário: "))
cars = int(input("Possui quantos carros?: "))
colors = str(input("Qual dessas cores de carro deseja?(Amarelo, Azul, Cinza): "))
models = str(input("Qual desses modelos de carro deseja?(Hatch, Sedan, Conversível): "))



if cars == 3:
  print("O Sr(a). já possui 3 carros.")
else:
  sql_cars = f"INSERT into cars (id, colors, models, owner_id) value ('1', '{colors}', '{models}', '1' )"
  main.insert_db(sql_cars)

