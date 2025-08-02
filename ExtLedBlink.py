from machine import Pin 
import time

BoardLed = Pin("LED", Pin.OUT)
BoardLed.value(1)

led = Pin (21, Pin.OUT)

while True:
    led.toggle()
    time.sleep(0.5)