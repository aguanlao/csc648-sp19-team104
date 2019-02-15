import psycopg2

hostname = "localhost"
username = "admin"
password = "justD0it!"
db = "pegasus-dev"
conn_string = "dbname='%s' user='%s' host='%s' password='%s'" % (db, username, hostname, password)

conn = psycopg2.connect(conn_string)
print("Done")