import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "hjh",
    password = "hjh"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE test")