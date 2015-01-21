#! /usr/bin/env python3

##################
### speed control
##################

import sys
import RPi.GPIO as GPIO
from time import sleep
sys.path.append(r'/opt/quick2wire-python-api')
from quick2wire.parts.pcf8591 import *
from quick2wire.i2c import I2CMaster

### pcf8591
### BASE_ADDRESS is 0x48 default
address = int(sys.argv[1]) if len(sys.argv) > 1 else BASE_ADDRESS
pin_index = int(sys.argv[2]) if len(sys.argv) > 2 else 0

### l298n
### en[a|b][0|1] pins enable the motor
### trigger waits for high from OR gate
###########
##########
### can enb0 & 1 be tied togeather??????
enb0 = int(19)
enb1 = int(26)
trigger = int(20)

### pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(enb0, GPIO.OUT)
GPIO.setup(enb1, GPIO.OUT)
GPIO.setup(trigger, GPIO.IN)

def halt_pwm():
  pwma0.stop()
  pwma1.stop()

def set_pwm():
  with I2CMaster() as i2c:
    adc = PCF8591(i2c, FOUR_SINGLE_ENDED)
    sei = adc.single_ended_input_count()
    print('single ended input count: %s' % sei)
    aout = adc.output()
    print('AOUT: %s' % aout)
    ### assuming 'pin' is AIN0?
    pin = adc.single_ended_input(pin_index)
    
    while True:
      pinval = int(pin.value * 100)
      pinval = int(1) if pinval < int(1) else pinval
      print(pinval)
      pwma0 = GPIO.PWM(enb0, pinval)
      pwma1 = GPIO.PWM(enb1, pinval)
      pwma0.start(15)
      pwma1.start(15) 
      #print("read: {} : {}".format(count, pin.value))
      sleep(0.5)

GPIO.add_event_detect(trigger, GPIO.RISING, callback=set_pwm, bouncetime=200)
GPIO.add_event_detect(trigger, GPIO.FALLING, callback=halt_pwm, bouncetime=200)
