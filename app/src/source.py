import app.main as main
from flask import Flask, request
from app.models.cars import Car
from app.models.owner import Owner
import request

app = Flask(__name__)
main.conn_db()

@app.route('/', methods=['GET'])
def home():
    return "Welcome, Home!"

@app.route('/owners', methods=['GET'])
def owner():
    sql = ''' select * from owners'''
    reg = main.consult_db(sql)
    return reg

@app.route('/cars', methods=['GET'])
def cars():
    sql = ''' select * from cars'''
    reg = main.consult_db(sql)
    return reg

@app.route('/owners/register', methods=['POST'])
def register_owner():
    car = Car()
    owner = Owner()
    if owner.qtd_cars == 3:
        print("Proprietário já possui 3 carro.")
    else:
        sql = f'''insert into owner (id, name, quantity_cars, model_cars, colors_cars) value ('{+1}','{owner.name}', '{owner.qtd_cars}', '{owner.models}', '{owner.colors}')'''
        reg = main.insert_db(sql)
        return reg
@app.route('/cars/register', methods=['POST'])
def register_cars():
    car = Car()
    if

if __name__ == '__main__':
    app.run(debug=True)