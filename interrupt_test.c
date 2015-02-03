#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <error.h>
#include <unistd.h>

#include <wiringPi.h>
#include <softPwm.h>
#include <pcf8591.h>

#define ENB0 19
#define ENB1 26
#define JOYSTICK 20 //input
#define RANGE 100  //pwm range
#define PINBASE 120  //pcf pinbase

/*
test by running the following:

sudo gpio -g mode 20 up
sudo gpio -g mode 20 down

*/

//prototypes
void blink (void);
void start_pwm (void);
void stop_pwm (void);


int main (void) {
  unsigned int usecs;
  usecs = 100;

  wiringPiSetupGpio();
  pinMode(ENB0, OUTPUT);
  pinMode(ENB1, OUTPUT);
  pinMode(JOYSTICK, INPUT);

  softPwmCreate(ENB1, 1, RANGE); //pin, initial value, range

  pcf8591Setup(PINBASE, 0x48);

  wiringPiISR(JOYSTICK, INT_EDGE_BOTH, start_pwm);

  while(1) {
    //printf("waiting for int..."); fflush(stdout);
    usleep(usecs);
  }

  return(0);

}


//while i'm high...
void start_pwm(void) {
  printf("start_pwm...\n");
  //pwm_freq is read from AIN0
  int pwm_freq;
  while(1) {
    pwm_freq = analogRead(PINBASE + 0); //AIN0
    pwm_freq = pwm_freq / 2.55;
    printf("pwm: %d\n", pwm_freq);
    //softPwmWrite(ENB1, pwm_freq); //writing pwm freq to L298N
    delay(500);
    //test if JOYSTICK is low
    if(digitalRead(JOYSTICK) == 0) {
      break;
    }
  }

}
