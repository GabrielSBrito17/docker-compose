import psycopg2
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

def insert_db(sql):
    con = conn_db()
    cur = con.cursor()
    try:
        cur.execute(sql)
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    cur.close()

def consult_db(sql):
    con = conn_db()
    cur = con.cursor()
    cur.execute(sql)
    recset = cur.fetchall()
    registros = []
    for rec in recset:
        registros.append(rec)
    con.close()
    return registros

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