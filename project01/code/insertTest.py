import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "hjh",
    password = "hjh",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("YANG", "Highway 21")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted")