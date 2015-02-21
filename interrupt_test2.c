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
#define JSL 20 //joystick input left
#define JSR 21 //joystick input right
#define RANGE 100  //pwm range
#define PINBASE 120  //pcf pinbase

/*
test by running the following:

sudo gpio -g mode 20 up
sudo gpio -g mode 20 down
*/

//prototypes
void start_pwm (void);


int main (void) {
  unsigned int usecs;
  usecs = 100;

  wiringPiSetupGpio();
  pinMode(ENB0, OUTPUT); //sw pwm
  pinMode(ENB1, OUTPUT);
  digitalWrite(ENB0, 0); //init as low
  digitalWrite(ENB1, 0); //init as low
  //pinMode(ENB1, PWM_OUTPUT); //if using hw pwm
  pinMode(JSL, INPUT);
  pinMode(JSR, INPUT);
  digitalWrite(JSL, 0); //init as low
  digitalWrite(JSR, 0); //init as low

  //softPwmCreate(ENB0, 1, RANGE); //pin, initial value, range
  softPwmCreate(ENB1, 1, RANGE); //pin, initial value, range

  pcf8591Setup(PINBASE, 0x48);

  wiringPiISR(JSL, INT_EDGE_BOTH, start_pwm);
  wiringPiISR(JSR, INT_EDGE_BOTH, start_pwm);

  while (1) {
    usleep(usecs);
  }

  return(0);

}


//while i'm high...
void start_pwm(void) {
  //printf("start_pwm...\n");
  //pwm_freq is read from AIN0
  int pwm_freq;
  while (1) {
    //test if JOYSTICK is low
    if (digitalRead(JSL) == 0 && digitalRead(JSR) == 0) {
      printf("\njoystick released\n");
      digitalWrite(ENB0, 0);
      digitalWrite(ENB1, 0);
      break;
    }

    pwm_freq = analogRead(PINBASE + 0) / 2.55; //AIN0
    if (pwm_freq == 0) {
      pwm_freq = 1;
    }
    printf("\rpwm: %d", pwm_freq);
    fflush(stdout);
    //softPwmWrite(ENB0, pwm_freq); //writing pwm freq to L298N
    softPwmWrite(ENB1, pwm_freq); //writing pwm freq to L298N
    //pwmWrite(); //hw pwm bcm port 18 range 0-1024
    //digitalWrite(ENB0, 1);
    delay(500);
  }

}
