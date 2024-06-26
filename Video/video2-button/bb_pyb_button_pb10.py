# bb_pyb_button_pb10.py
#
# Copyright (C) 2024 KW Services.
# MIT License
# MicroPython 1.20
#
from pyb import Pin, LED
import time

# Builtin LED on the BlackPill.
led = LED(1)
led.off()

key = Pin("PB10", Pin.IN, Pin.PULL_UP)

print("User button defined at {}.".format(key))
done = False
while not done:
    key_btn = key.value()   # returns one or zero.
    #print("key_btn:",key_btn)
    if key_btn == 0:
        led.on()
        time.sleep(0.5)
    led.off()
    time.sleep(0.5)

