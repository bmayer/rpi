# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <error.h>

# include <wiringPi.h>
# include <softPwm.h>
# include <pcf8591.h>

# define ENB0 19
# define ENB1 26
# define TRIGGER 20
# define RANGE 100  //pwm range
# define PINBASE 120  //pcf pinbase

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

  wiringPiISR(TRIGGER, INT_EDGE_RISING, blink);

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


void start_pwm(void) {
  printf("start_pwm...\n");
  //pwm_freq is read from AIN0
  double pwm_freq;
  pwm_freq = analogRead();
  softpwmWrite(ENB1, pwm_freq);


}
