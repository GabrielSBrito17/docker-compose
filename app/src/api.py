from flask import Flask, request, render_template
from app.index import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome, Home!"

@app.route('/owners', methods=['GET'])
def owner():
    main.conn_db()
    # sql = ''' select * from owners'''
    reg = main.consult_db("owners")
    return reg

@app.route('/cars', methods=['GET'])
def cars():
    main.conn_db()
    sql = ''' select * from cars'''
    reg = main.consult_db(sql)
    return reg

@app.route('/owners/register', methods=['POST'])
def register_owner():
    # car = Car()
    main.conn_db()
    owner = Owner()
    try:
        if owner.qtd_cars == 3:
            print("Proprietário já possui 3 carro.")
        else:
            # sql = f'''insert into owners (id, name, quantity_cars, model_cars, colors_cars) values ('{owner.id}','{owner.name}', '{owner.qtd_cars}', '{owner.models}', '{owner.colors}')'''
            main.insert_db(owner.id, owner.name, owner.qtd_cars, owner.models, owner.colors)
        # sql = f''' select * from owners order by {owner.name}'''
        reg = main.consult_db(f"{owner.name}")
        return list(reg)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(debug=True)