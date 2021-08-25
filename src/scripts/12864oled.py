from machine import Pin, I2C
from src.modules.ssd1306 import SSD1306_I2C
from src.modules.DHT22 import DHT22
import utime as time

WIDTH = 128
HEIGHT = 64

i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=100000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
print("I2C Address        : "+hex(i2c.scan()[0]).upper())
print("I2C Configuration  : "+str(i2c))

dht_data = Pin(15,Pin.IN,Pin.PULL_UP)
dht_sensor=DHT22(dht_data,Pin(14,Pin.OUT),dht11=False)

while True:
    T,H = dht_sensor.read()
    #Converted to Fahrenheit (FT) for LCD display
    FT = T*1.8+32
    if T is None:
        print(" sensor error")
    else:
        print("{:3.1f}'C  {:3.1f}%".format(T,H))
    #DHT22 not responsive if delay too short
    time.sleep_ms(250)
    
    oled.fill(1)
    oled.text("PICO HYGROMETER",4,6,0)

    oled.text("TEMPERATURE",4,20,0)
    # If using Celsius, change (FT) to (T) and "F" to "C" on line below
    oled.text(str('%.1f'%FT),14,29,0)
    oled.text("FAHRENHEIT",60,29,0)

    oled.text("HUMIDITY",4,42,0)
    oled.text(str('%.1f'%H),14,51,0)
    oled.text("PERCENT",60,51,0)

    oled.show()
    time.sleep_ms(250)
