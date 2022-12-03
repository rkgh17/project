import time
import Adafruit_DHT

sensor = Adafruit_DHT.DTH22
pin = 4
try:
        while True:
                h, t = Adafruit_DHT.read_retry(sensor.pin)
                if h is not None and t is not None:
                        print(f"Temperature = {t}*C Humidity = {h}%")
                else:
                        print('Read error')
                time.sleep(1)

except Keyboardinterrupt:
        print("Terminated by Keyboard")
finally:
        print("End of Program")
