import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "hjh",
    password = "hjh",
    database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255))")