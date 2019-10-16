import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="route",
  database="kelly_db"
)

mycursor = mydb.cursor()

sql = "INSERT INTO products (id , name) VALUES (%s, %s)"
val = [
    (152,"X"),
    (153,"Y"),
    (154,"Z")
  
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
