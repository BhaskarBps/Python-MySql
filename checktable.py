import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="route",
  database="kelly_db"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
