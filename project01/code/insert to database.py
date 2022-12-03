import time
import board
import adafruit_dht
import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "hjh",
    password = "hjh",
    database = "test"
)#데이터베이스 연결 정보

mycursor = mydb.cursor()
dhtDevice = adafruit_dht.DHT22(board.D4)
sql="insert into RAS(DEV, TIME, TEMP, HUMI) values(%s, %s, %s, %s)"

while True:
        try:
                temp = dhtDevice.temperature
                humi = dhtDevice.humidity
                val = ("DHT22", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), temp, humi)

                mycursor.execute(sql, val)
                mydb.commit()#데이터베이스에 센서값과 시간값 저장

        except RuntimeError as error:
                print(error.args[0])
                time.sleep(2.0)
                continue
        except Exception as error:
                dhtDevice.exit()
                raise error
        time.sleep(2.0)