import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="route",
  database="kelly_db"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
