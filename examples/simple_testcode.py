#5up Digital Input v1.0p test code

from machine import Pin
from pyb import CAN, ADC
import utime


print("starting digital input x5 board test")
print("v1.0")
print("initializing")
can = CAN(1, CAN.NORMAL)
can.setfilter(0, CAN.LIST16, 0, (123, 124, 125, 126))


#Setup Pins
hbt_led = Pin("D5", Pin.OUT)
func_butt = Pin("E7", Pin.IN, Pin.PULL_UP) 

input_a = Pin("D1", Pin.IN)
input_b = Pin("E2", Pin.IN)
input_c = Pin("E1", Pin.IN)
input_d = Pin("D0", Pin.IN)
input_e = Pin("E3", Pin.IN)


#Setup hbt timer
hbt_state = 0
hbt_interval = 500
start = utime.ticks_ms()
next_hbt = utime.ticks_add(start, hbt_interval)
hbt_led.value(hbt_state)


print("starting")


def chk_hbt():
    global next_hbt
    global hbt_state
    now = utime.ticks_ms()
    if utime.ticks_diff(next_hbt, now) <= 0:
        if hbt_state == 1:
            hbt_state = 0
            hbt_led.value(hbt_state)
            #print("hbt")
        else:
            hbt_state = 1
            hbt_led.value(hbt_state)  
        
        next_hbt = utime.ticks_add(next_hbt, hbt_interval)

def chk_buttons():
    global next_button_chk
    now = utime_ms()
    if utime.ticks_diff(next_button_chk, now) <= 0:
        pass
        

def send():
    can.send('EVZRTEST', 123)   # send a message with id 123
    
def get():
    mess = can.recv(0)
    print(mess)
    blink_fast()
        
def blink_fast():
    for i in range(30):
        hbt_led.value(1)
        utime.sleep_ms(50)
        hbt_led.value(0)
        utime.sleep_ms(50)
      
while True:
    chk_hbt()
    if not (func_butt.value()):
        print("function button")
        blink_fast()
        send()
        utime.sleep_ms(200)
    
    if(can.any(0)):
        get()
    
    
    if not (input_a.value()):
        print("input_a triggered")
        utime.sleep_ms(200)
    if not (input_b.value()):
        print("input_b triggered")
        utime.sleep_ms(200)
    if not (input_c.value()):
        print("input_c triggered")
        utime.sleep_ms(200)
    if not (input_d.value()):
        print("input_d triggered")
        utime.sleep_ms(200)
    if not (input_e.value()):
        print("input_e triggered")
        utime.sleep_ms(200)
        
    
    
    
    
