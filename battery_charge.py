from machine import Pin, SoftI2C
import time
from ssd1306 import SSD1306_I2C
import machine

i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled = SSD1306_I2C(128, 64, i2c)
#white frame 1 battery
oled.fill_rect(5,5,30,50,1)
#black filling 1 battery
oled.fill_rect(7,7,26,46,0)

#white frame 2 battery
oled.fill_rect(45,5,30,50,1)
#black filling 2 battery
oled.fill_rect(47,7,26,46,0)
#white filling = charge 100% 1 battery
oled.fill_rect(9,9,22,42,1)

#number 1 battery charge in the beginning
battery_1_percentage = 0
battery_1_delta = 1

y_min = 9
y_max = 50

while True:
    # drawing
    #refresh black backgroung 1 battery numbers
    oled.fill_rect(5,57,30,15,0)
    #refresh black backgroung 2 battery numbers
    oled.fill_rect(45,57,30,15,0)
    #numbers 1 battery
    oled.text(str(100-battery_1_percentage),5,57)
    #numbers 2 battery
    oled.text(str(battery_1_percentage),45,57)

    # filling the batteries
    y_cur_1 = battery_1_percentage * (y_max - y_min) / 100 + y_min
    y_cur_2 = y_min + (y_max - y_cur_1)
    if y_cur_1 > y_min and y_cur_1 < y_max:
        oled.hline(9, int(y_cur_1), 22, 0 if (battery_1_delta > 0) else 1)
    if y_cur_2 > y_min and y_cur_2 < y_max:
        oled.hline(49, int(y_cur_2), 22, 1 if (battery_1_delta > 0) else 0)

    # direction change
    battery_1_percentage += battery_1_delta
    if battery_1_percentage <= 0 or battery_1_percentage >= 100:
        battery_1_delta *= -1
    

    oled.show()
    time.sleep(0.5)