# https://stackoverflow.com/questions/22112657/how-install-and-configure-mysql-5-6-16-in-windows-7
# https://dev.mysql.com/downloads/
# MySQL Community Server
#

# https://www.w3schools.com/python/python_mysql_getstarted.asp
# https://www.w3schools.com/python/python_mysql_create_db.asp

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="tacos")

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
