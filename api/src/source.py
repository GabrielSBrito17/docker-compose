import app.main as main
from flask import Flask
import psycopg2

app = Flask(__name__)
main.conn_db()

@app.route('/', methods=['GET'])
def home():
    return "Welcome, Home!"

@app.route('/owner', methods=['POST'])
def owner():
    sql = ''' select * from owner'''
    main.consult_db(sql)
    return "Sucesso"

@app.route('/cars/models', methods=['GET'])
def cars():
    return

if __name__ == '__main__':
    app.run(debug=True)