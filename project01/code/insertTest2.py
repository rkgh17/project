import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "hjh",
    password = "hjh",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

val = [
    ('CHOI', 'Lowstreet4'),
    ('YangCHOI', 'ulsan'),
    ('BAEK', 'busan'),
    ('PARK', 'seoul'),
    ('HAN', 'jinju')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record was inserted")