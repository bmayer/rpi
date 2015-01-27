#include <stdio.h>
#include <wiringPi.h>
#include <pcf8591.h>

#define PINBASE 120 //must be > 64

//read the analogue input from a potentiometer


int main(void) {
  int pin = 20;
  double pin_val;

  wiringPiSetupGpio();
  pcf8591Setup(PINBASE, 0x48);

  while(1)
  {
    pin_val = analogRead(pin);
    printf("pin_val: %5.2f\n", pin_val);
    delay(500); //ms
  }

}
