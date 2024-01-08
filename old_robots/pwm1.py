import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

# gpio 24 @ 50Hz
m1 = GPIO.PWM(24, 50)

# 50% duty cycle
# can be between 0.0 - 100.0%
p1.start(50)
time.sleep(5)

m1.ChangeFrequency(75)
time.sleep(5)

m1.ChangeDutyCycle(35)
time.sleep(3)

p.stop()

GPIO.cleanup()
