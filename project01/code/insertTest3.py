import RPi.GPIO as GPIO
import time
import board
import adafruit_dht
import sys
import pymysql

dhtDevice = adafruit_dht.DHT22(board.D4)
conn = pymysql.connect(host="localhost", user="hjh", passwd="hjh", db="test")
try:
    with conn.cursor() as cur:
        sql="insert into DHT22(DEV, TIME, TEMP, HUMI) values(%s, %s, %s, %s)"
        while True:
            print("temp")
            temperature = dhtDevice.temperature
            time.sleep(5)
            print("humi")
            humidity = dhtDevice.humidity
            time.sleep(5)
            print("insert start")
            if humidity is not None and temperature is not None:
                cur.execute(sql,("DHT22", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), temperature, humidity))
                conn.commit()
            else:
                print("Failed to get readint.")
            time.sleep(10)
except KeyboardInterrupt:
    exit()
finally:
    conn.close()