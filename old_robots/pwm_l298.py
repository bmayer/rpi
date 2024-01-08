
import RPi.GPIO as GPIO
import time

delay = 0.2
steps = int(500)

ea = 17
a1 = 24
a2 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(ea, GPIO.OUT)
GPIO.setup(a1, GPIO.OUT)
GPIO.setup(a2, GPIO.OUT)

#set ea to 50hz
enable_a = GPIO.PWM(17, 50)
print 'enable_a @50Hz with 50% Duty Cycle'
enable_a.start(50) # 50% duty cycle


enable_a.ChangeFrequency(20)
print 'enable_a @20Hz'

enable_a.ChangeDutyCycle(75)
print 'enable_a 75% Duty Cycle'

print 'A1/A2 stepping...'
for step in range(500):
  GPIO.output(a1, 1)
  GPIO.output(a2, 0)
  time.sleep(delay)
  GPIO.output(a1, 0)
  GPIO.output(a2, 1)
  time.sleep(delay)

GPIO.cleanup()
