
import RPi.GPIO as GPIO
import time

# use with L298N motor driver

# en* pins enable the motor
ena0 = 17 #outside pin (blue)
ena1 = 18 #outside pin (blue)

# in* pins control the direction
in1 = 24 #(white)
in2 = 25 #(orange) 

# output A pins connect to DC motor
# +12v input can actually be any input voltage
# ground of dc motor power source connects to GND on L298
# this ground also needs to tie into the pi GND

sleep = 1.5

GPIO.setmode(GPIO.BCM)

# set up pi gpio pins as outs
GPIO.setup(ena0, GPIO.OUT)
GPIO.setup(ena1, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

# set both enable A pins to HIGH
# set pin & freq
ena0_pwm = GPIO.PWM(ena0, 10)
ena1_pwm = GPIO.PWM(ena1, 10)
# set duty cycle
ena0_pwm.start(5)
ena1_pwm.start(5)

# controlling the motor direction
#while True:
for step in range(10):
  print 'step: %s' % (step)
  GPIO.output(in1, 1)
  GPIO.output(in2, 0)
  time.sleep(sleep)
  GPIO.output(in1, 0)
  GPIO.output(in2, 1)
  time.sleep(sleep)

GPIO.cleanup()
