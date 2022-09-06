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

def create_db(sql):
    con = conn_db()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()
    return print("sucesso")

def insert_db(id=None, name=None, qtd_cars=None, models=None, colors=None):
    con = conn_db()
    cur = con.cursor()
    count = id
    try:
        sql = f'''insert into owners (id, name, quantity_cars, model_cars, colors_cars) values ('{int(id)}','{name}', '{int(qtd_cars)}', '{models}', '{colors}')'''
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

def consult_db(data, table):
    con = conn_db()
    cur = con.cursor()
    sql = f'''select * from owners where '{data}' in '{table}' '''
    cur.execute(sql)
    con.commit()
    recset = cur.fetchall()
    df = pd.DataFrame(recset, columns=["id", "name", "quantity_cars", "model_cars", "colors_cars"])
    con.close()
    return df.to_json()

def filter_db(filter):
    con = conn_db()
    cur = con.cursor()
    sql = f'''select '{filter}' from owners '''
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

def update_db(sale, name):
    con = conn_db()
    cur = con.cursor()
    sql = f'''UPDATE owners SET quantity_cars = {sale} WHERE id = '{name}' '''
    cur.execute(sql)
    con.commit()
    con.close()
    return "Atualizado com sucesso!!"

# db = update_db(2, 1)
# print(db)
# sql = '''CREATE TABLE cars
#       ( id            character varying(500),
#         colors           character varying(500),
#         models          character varying(500),
#         owner_id  character varying(500),
#         PRIMARY KEY (ID)
#       )'''
# create_db(sql)
# sql = '''CREATE TABLE owners
#       ( id            character varying(500),
#         name           character varying(500),
#         quantity_cars          character varying(500),
#         model_cars  character varying(500),
#         colors_cars  character varying(500),
#         PRIMARY KEY (ID)
#       )'''
# create_db(sql)

# sql = """
#     INSERT into public.deputados (id, colors, models, owner_id) value
#     values('%s','%s','%s','%s','%s','%s','%s','%s','%s');
#     """
# insert_db(sql)

# reg = consult_db('select * from cars')
# df_bd = pd.DataFrame(reg, columns=["id", "colors", "models", "owner_id"])
# print(df_bd)
# print('conectado')