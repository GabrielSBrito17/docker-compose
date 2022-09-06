import psycopg2
import json
import pandas as pd

host = '172.20.48.1'
dbname = 'carros_db'
user = "root"
password = "123456"
sslmode = 'disable'
port = "5432"

def conn_db():
    conn_string = "host={0} dbname={1} password={2} sslmode={3} port={4} user= {5}".format(host, dbname, password, sslmode, port, user)
    conn = psycopg2.connect(conn_string)
    return conn

def create_db_init(sql):
    con = conn_db()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()
    return print("Criou o banco com sucesso!")

def create_db(sql):
    con = conn_db()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    recset = cur.fetchall()
    df = pd.DataFrame(recset, columns=[str("id"), "name", "quantity_cars", "model_cars", "colors_cars"])
    con.close()
    return df.to_json()

def insert_db(id=None, name=None, qtd_cars=None, models=None, colors=None):
    con = conn_db()
    cur = con.cursor()
    count = id
    try:
        sql = f'''insert into owners (id, name, quantity_cars, model_cars, colors_cars) values ('{id}','{name}', '{qtd_cars}', '{models}', '{colors}')'''
        cur.execute(sql)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    recset = cur.fetchall()
    df = pd.DataFrame(recset, columns=["id", "name", "quantity_cars", "model_cars", "colors_cars"])
    con.close()
    return df.to_json()

def consult_db(data, value):
    con = conn_db()
    cur = con.cursor()
    sql = f'''select * from owners where '{data}' in ('{value}') '''
    cur.execute(sql)
    con.commit()
    recset = cur.fetchall()
    df = pd.DataFrame(recset, columns=[f"{data}"])
    con.close()
    return df.to_json()

def filter_db(filter):
    con = conn_db()
    cur = con.cursor()
    sql = f'''select id, name, quantity_cars, model_cars, colors_cars from owners where name in ('{filter}')'''
    cur.execute(sql)
    con.commit()
    recset = cur.fetchall()
    df = pd.DataFrame(recset, columns=["id", "name", "quantity_cars", "model_cars", "colors_cars"])
    return df

def delete_db(filter):
    con = conn_db()
    cur = con.cursor()
    try:
        sql = f"""DELETE FROM owners WHERE id = '{str(filter)}';"""
        cur.execute(sql)
        con.commit()
    except Exception as e:
        print(e)
    # recset = cur.fetchall()
    # df = pd.DataFrame(recset, columns=["id", "name", "quantity_cars", "model_cars", "colors_cars"])
    con.close()
    return "Deletou"

def update_db(data, value, id):
    con = conn_db()
    cur = con.cursor()
    sql = f'''UPDATE owners SET {data} = '{str(value)}' WHERE id = '{id}' '''
    cur.execute(sql)
    con.commit()
    con.close()
    return "Atualizado com sucesso!!"


# sql = '''CREATE TABLE owners
#       ( id            integer,
#         name           varchar,
#         quantity_cars          integer,
#         model_cars  varchar,
#         colors_cars  varchar,
#         PRIMARY KEY (ID)
#       )'''
# create_db_init(sql)