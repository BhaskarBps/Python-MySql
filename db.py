import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="route"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE kelly_db")
