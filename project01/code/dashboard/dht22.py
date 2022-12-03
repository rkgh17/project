import time
import Adafruit_DHT
import mysql.connector

mydb = mysql.connector.connect(
    host = "18.224.252.11",
    user = "hjh",
    password = "hjh",
    database = "test"
)

sensor = Adafruit_DHT.DHT22
pin = 4
mycursor = mydb.cursor()

sql="insert into DHT22(DEV, TIME, TEMP, HUMI) values(%s, %s, %s, %s)"

try:
        while True:
                h, t = Adafruit_DHT.read_retry(sensor, pin)
                val = ("DHT22", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), t, h)
                mycursor.execute(sql, val)
                mydb.commit()
except KeyboardInterrupt:
    print("Terminated by Keyboard")
finally:
    print("End of Program")