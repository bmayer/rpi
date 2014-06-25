
import RPi.GPIO as GPIO
import time

# use with L298N motor driver

# en* pins enable the motor
ena0 = 17 #outside pin
ena1 = 18 #inside pin

# in* pins control the direction
in1 = 24
in2 = 25

sw0 = 22
sw1 = 7

# output A pins connect to DC motor
# +12v input can actually be any input voltage
# ground of dc motor power source connects to GND on L298
# this ground also needs to tie into the pi GND

sleep = 1.5

GPIO.setmode(GPIO.BCM)

# set up pi gpio pins
GPIO.setup(ena0, GPIO.OUT)
GPIO.setup(ena1, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(sw0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# set enable pins & freq
ena0_pwm = GPIO.PWM(ena0, 10)
ena1_pwm = GPIO.PWM(ena1, 10)

def stop_motor(*args):
  print 'sw1 stop rx'
  for arg in args:
    print 'arg: %s' % (arg)

  ena0_pwm.stop()
  ena1_pwm.stop()
  GPIO.cleanup()
  exit()

#GPIO.add_event_detect(sw1, GPIO.BOTH, callback=stop_motor, bouncetime=300)
GPIO.add_event_detect(sw1, GPIO.FALLING, callback=stop_motor, bouncetime=300)

# controlling the motor direction
while True:
  GPIO.wait_for_edge(sw0, GPIO.FALLING)
  if GPIO.input(sw0):
    print 'sw0 detected'
    # set duty cycle
    ena0_pwm.start(5)
    ena1_pwm.start(5)
    for step in range(10):
      print 'step: %s' % (step)
      GPIO.output(in1, 1)
      GPIO.output(in2, 0)
      time.sleep(sleep)
      GPIO.output(in1, 0)
      GPIO.output(in2, 1)
      time.sleep(sleep)

  ena0_pwm.stop()
  ena1_pwm.stop()

GPIO.cleanup()
