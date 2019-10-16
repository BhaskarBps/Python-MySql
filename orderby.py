import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="route",
  database="kelly_db"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name desc"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
