import psycopg2

host = 'localhost'
dbname = 'db'
user = "postgre"
password = "postgre"
sslmode = 'disable'
port = "5433"

conn_string = "host={0} dbname={1} password={2} sslmode={3} port={4} user= {5}".format(host, dbname, password, sslmode, port, user)
conn = psycopg2.connect(conn_string)
print('conectado')