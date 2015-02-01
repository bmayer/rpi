# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <error.h>

# include <wiringPi.h>
# include <softPwm.h>
# include <pcf8591.h>

# define ENB0 19
# define ENB1 26
# define TRIGGER 20 //input - joy-stick
# define RANGE 100  //pwm range
# define PINBASE 120  //pcf pinbase

/*
test buy running the following:

sudo gpio -g mode 20 up
sudo gpio -g mode 20 down

*/

//prototypes
void blink (void);
void start_pwm (void);
void stop_pwm (void);


int main (void) {
  wiringPiSetupGpio();
  pinMode(ENB0, OUTPUT);
  pinMode(ENB1, OUTPUT);
  pinMode(TRIGGER, INPUT);

  softPwmCreate(ENB1, 1, RANGE); //pin, initial value, range

  pcf8591Setup(PINBASE, 0x48);

  wiringPiISR(TRIGGER, INT_EDGE_BOTH, start_pwm);

  while(1) {
    //printf("waiting for int..."); fflush(stdout);
  }

  return(0);

}


void blink(void) {
  printf("blinky...\n");

  int x;
  for(x=0; x<10; ++x) {
    digitalWrite(ENB0, HIGH);
    delay(500);
    digitalWrite(ENB0, LOW);
  }

}

//while i'm high...
void start_pwm(void) {
  printf("start_pwm...\n");
  //pwm_freq is read from AIN0
  double pwm_freq;
  while(1) {
    pwm_freq = analogRead(PINBASE + 0); //AIN0
    printf("pwm: %5.2f\n", pwm_freq);
    //softpwmWrite(ENB1, pwm_freq); //writing pwm freq to L298N
    delay(500);
    //test if TRIGGER is low
    if(digitalRead(TRIGGER) == 0) {
      break;
    }
  }

}
