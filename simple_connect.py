import mysql.connector
import os

db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")


cnx = mysql.connector.connect(user=db_user, password=db_pass',
                              host=db_host,
                              database=db_name)
cnx.close()
