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

reg = consult_db('select * from cars')
df_bd = pd.DataFrame(reg, columns=["id", "colors", "models", "owner_id"])
print(df_bd)
# print('conectado')