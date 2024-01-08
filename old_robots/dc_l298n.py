
import RPi.GPIO as GPIO
import time

# use with L298N motor driver

# en* pins enable the motor
#ena0 = 18 #outside pin (blue)
ena0 = int(18) #outside pin (blue)
ena1 = int(27) #inside pin(21 on pi crust) (green)

# in* pins control the direction
in1 = int(24) #(white)
in2 = int(25) #(orange) 

# output A pins connect to DC motor
# +12v input can actually be any input voltage
# ground of dc motor power source connects to GND on L298
# this ground also needs to tie into the pi GND

sleep = 0.8

GPIO.setmode(GPIO.BCM)

# set up pi gpio pins as outs
GPIO.setup(ena0, GPIO.OUT)
GPIO.setup(ena1, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

# set both enable A pins to HIGH
#GPIO.output(ena0, 1)
#GPIO.output(ena1, 1)

GPIO.output(in1, 1)
GPIO.output(in2, 0)

pwma0 = GPIO.PWM(ena0, 10)
pwma1 = GPIO.PWM(ena1, 10)
pwma0.start(15)
pwma1.start(15)

#GPIO.output(in1, 0)
#GPIO.output(in2, 1)
time.sleep(5)

print 'chdir'
pwma0.stop()
pwma1.stop()
GPIO.output(in1, 0)
GPIO.output(in2, 0)
time.sleep(1)

pwma0 = GPIO.PWM(ena0, 10)
pwma1 = GPIO.PWM(ena1, 10)
pwma0.start(5)
pwma1.start(5)
GPIO.output(in1, 0)
GPIO.output(in2, 1)
time.sleep(5)

GPIO.output(in1, 0)
GPIO.output(in2, 0)
pwma0.stop()
pwma1.stop()

# controlling the motor direction
#while True:
"""
for step in range(10):
  #pwma0.ChangeFrequency(25)
  #pwma1.ChangeFrequency(25)
  GPIO.output(in1, 1)
  GPIO.output(in2, 0)
  time.sleep(sleep)
  print 'change dir'
  GPIO.output(in1, 0)
  GPIO.output(in2, 1)
  time.sleep(sleep)
"""

GPIO.cleanup()
