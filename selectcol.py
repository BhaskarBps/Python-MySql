import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="route",
  database="kelly_db"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
