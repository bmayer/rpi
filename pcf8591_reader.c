# include <stdio.h>
# include <wiringPi.h>
# include <pcf8591.h>

# define PINBASE 120 //must be > 64

//read the analogue input from a potentiometer


int main(void) {
  int pin = 0; //ain0
  double pin_val;

  wiringPiSetupGpio();  // enable bcm pin numbering
  pcf8591Setup(PINBASE, 0x48);

  while(1) {
    pin_val = analogRead(PINBASE + pin) / 2.55; //analog range 0 - 255, convert to 0 - 100
    pin_val = (pin_val == 0) ? pin_val = 1 : pin_val; //pwm doesnt allow 0
    printf("pin_val: %5.2f\n", pin_val);
    delay(500); //ms
  }

  return(0);

}
