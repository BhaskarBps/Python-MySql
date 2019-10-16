import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="route",
  database="kelly_db"
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers2"

mycursor.execute(sql)
