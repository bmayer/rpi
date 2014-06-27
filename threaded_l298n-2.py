
import RPi.GPIO as GPIO
import time


### L298N ENA* pins enable the motor(s)
### ENA* (ena0, ena1) pins can be jumpered together 
### on breadboard to save gpio pin usage
ena0 = 18 ### (green) ENA outside pin.

### L298N IN* pins change motor direction
### based upon switch input below
in1 = 22 ### (white)
in2 = 23 ### (orange)

### button to arm the L298N
arm = 

### SPDT switch
### GPIO INPUT pins
### swl = switch left 
### swr = switch right
swl = 17
swr = 27 ### (21 on PiCrust)

bt = 300 ### bouncetime
freq = int(raw_input('ENA freq: '))
duty = int(raw_input('ENA duty cycle: '))
sleep = int(raw_input('sleep: '))
steps = int(raw_input('steps: '))

GPIO.setmode(GPIO.BCM)
### input pins from switch are set to
### pull_down to prevent floating
GPIO.setup(arm, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(swl, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(swr, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ena0, GPIO.OUT) ### PWM pin
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)


### switch left
def swl_call():
  print 'swl action'
  ena0_pwm.start(duty)

  while 1:
    try:
      for step in steps:
        print 'step: %s' % (step)
        GPIO.output(in1, 1)
        GPIO.output(in2, 0)
        time.sleep(sleep)
        ena0_pwm.stop()

    except KeyboardInterrupt:
      pass


### switch right
def swr_call():
  print 'swr action'
  ena0_pwm.start(duty)

  while 1:
    try:
      for step in steps:
        print 'step: %s' % (step)
        GPIO.output(in1, 0)
        GPIO.output(in2, 1)
        time.sleep(sleep)
        ena0_pwm.stop()

    except KeyboardInterrupt:
      pass


### switch stop
def sw_stop():
  print 'switch falling'
  print 'stopping motor'
  ena0_pwm.stop()


### run ps -eLF to see if new threads appear
### can the callback value include vars?
### callback=swr_call(0,1)
print 'setting up interrupts\n'
#GPIO.add_event_detect(swl, GPIO.FALLING, callback=sw_stop, bouncetime=bt)
#GPIO.add_event_detect(swl, GPIO.RISING, callback=swl_call, bouncetime=bt)
#GPIO.add_event_detect(swr, GPIO.FALLING, callback=sw_stop, bouncetime=bt)
#GPIO.add_event_detect(swr, GPIO.RISING, callback=swr_call, bouncetime=bt)

GPIO.add_event_detect(swl, GPIO.RISING, callback=swl_call, bouncetime=bt)
GPIO.add_event_detect(swr, GPIO.RISING, callback=swr_call, bouncetime=bt)

try:
  while True:
    print 'waiting to be armed...'
    GPIO.wait_for_edge(arm, GPIO.RISING)
    print 'motor is armed'

except KeyboardInterrupt:
  ena0_pwm.stop()
  GPIO.cleanup()

finally:
  ena0_pwm.stop()
  GPIO.cleanup()


print 'ena %sHz/%s%% Duty Cycle' % (freq, duty)
ena0_pwm = GPIO.PWM(ena0, freq)

ena0_pwm.stop()
GPIO.cleanup()
