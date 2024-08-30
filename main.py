from machine import Pin,ADC
from utime import sleep_ms

# allotting pins
sen=Pin(15,Pin.IN)       # turbidity sens pin
buz=Pin(12,Pin.OUT)      # -ev pin of buzzer is connected
led=Pin(33,Pin.OUT)      # built-in led for esp32 cam module


while True:
    print("sen_v = ",sen.value())
    x=sen.value()
    print(x)
    if x==False:          # x less than 30 to detect defect
        buz.on()       # turn on buzzer
        led.value(0)   # turn on led
        sleep_ms(2000) # wait for 2 seconds
    else:
        buz.off()     # turn off buzzer 
        led.value(1)  # turn off led
    sleep_ms(100)