import sys
import main
import traceback
import pandas as pd


while True:
  try:
    owner = str(input("Nome do proprietário: "))
    people = main.filter_db(f"{owner}")
    if people.name.empty is False:
      cars = int(input("Possui quantos carros?: "))
      qtd_cars = main.filter_db(f"{owner}")
      if qtd_cars.quantity_cars[0] == 3:
        print("O Sr(a). já possui 3 carros.")
        sale = str(input("Deseja vender algum de seus carros? Yes/No")).upper()
        if sale == ('yes').upper():
          sales = - 1
          main.update_db("quantity_cars", sales, people.id[0])
        else:
          print("O(a) Sr(a). não pode ter mais carros.")
          break
      else:
        print(f"O Sr(a). possui {qtd_cars.quantity_cars[0]}, cor {qtd_cars.colors_cars[0]}, modelo {qtd_cars.model_cars[0]}")
        while True:
          colors = str(input("Qual dessas cores de carro deseja?(Amarelo, Azul, Cinza): "))
          color_car = main.filter_db(f"{owner}")
          if color_car.colors_cars[0] == colors:
            print("Você já possui carro dessa cor, tente outra.")
          else:
            main.update_db("colors_cars", colors, people.id[0])
            break
        while True:
          models = str(input("Qual desses modelos de carro deseja?(Hatch, Sedan, Conversível): "))
          model = main.filter_db(f"{owner}")
          if model.models_cars[0] == models:
            print("Você já possui carro desse modelo, tente outro.")
          else:
            main.update_db("models_cars", models, people.id[0])
            break
    else:
      people_id = people.id[0] + 1
      qtd_cars = 1
      main.insert_db(id=people_id, name=f"{owner}", qtd_cars="null", models="null", colors="null")
      while True:
        colors = str(input("Qual dessas cores de carro deseja?(Amarelo, Azul, Cinza): "))
        color_car = main.filter_db(f"{owner}")
        if color_car.colors_cars[0] == colors:
          print("Você já possui carro dessa cor, tente outra.")
        else:
          main.update_db("colors_cars", colors, people.id[0])
          break
      while True:
        models = str(input("Qual desses modelos de carro deseja?(Hatch, Sedan, Conversível): "))
        model = main.filter_db(f"{owner}")
        if model.models_cars[0] == models:
          print("Você já possui carro desse modelo, tente outro.")
        else:
          main.update_db("models_cars", models, people.id[0])
          break
      main.insert_db(id=people_id, name=f"{owner}", qtd_cars=f"{qtd_cars}", models=f"{models}", colors=f"{colors}")
  except Exception as e:
    traceback.print_exc()
    print(e)
    break

