#https://projects.drogon.net/raspberry-pi/wiringpi/the-gpio-utility/

#thanks a lot, with your help i got this stepper running:

#http://www.youtube.com/watch?v=yzzafSqnk5s&amp;

#controlling a stepper with raspberrypi gpio pins

#took a schmalzhaus easydriver stepper shield
#controlled with a little shell script

#Here,my stepper has 1,8° = 200 Steps for 360°
#GPIO pin 23 controlls the steps, one high peak per step,
#GPIO pin 24 controlls the direction

#30 times clockwise and counterclockwise Rounds:

#!/bin/sh
pause=0.001
gpio -g mode 23 out
gpio -g mode 24 out

for i in $(seq 30); do
  echo Runde $i startet:
  sleep 1
  gpio -g write 24 1
  
  for i in $(seq 200); do
    echo $i
    gpio -g write 23 1
    sleep $pause
    gpio -g write 23 0
    sleep $pause
  done
  
  sleep 1
  gpio -g write 24 0
  
  for i in $(seq 200); do
    echo $i
    gpio -g write 23 1
    sleep $pause
    gpio -g write 23 0
    sleep $pause
  done
done

