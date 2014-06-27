
import RPi.GPIO as GPIO
import time

# use with L298N motor driver

# en* pins enable the motor
ena0 = 18 #outside pin (blue)
ena1 = 27 #inside pin (green)

# in* pins control the direction
in1 = 22 #(white)
in2 = 23 #(orange) 

# output A pins connect to DC motor
# +12v input can actually be any input voltage
# ground of dc motor power source connects to GND on L298
# this ground also needs to tie into the pi GND

sleep = 0.5

GPIO.setmode(GPIO.BCM)

# set up pi gpio pins as outs
GPIO.setup(ena0, GPIO.OUT)
GPIO.setup(ena1, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

# set both enable A pins to HIGH
GPIO.output(ena0, 1)
GPIO.output(ena1, 1)

# controlling the motor direction
#while True:
for step in range(10):
  GPIO.output(in1, 1)
  GPIO.output(in2, 0)
  time.sleep(sleep)
  GPIO.output(in1, 0)
  GPIO.output(in2, 1)
  time.sleep(sleep)

GPIO.cleanup()
