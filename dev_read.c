# include <stdio.h>
# include <stdint.h>
# include <fcntl.h>
# include <unistd.h>
# include <sys/ioctl.h>

// read from /dev/urandom 10 times

int main(void) {
  int a = 0;
  unsigned int rand;
  unsigned int *r; //i am a pointer to an integer var
  char *dev = "/dev/urandom";
  int myfile = open(dev, O_RDONLY);

  // &rand is an address operator
  r = &rand;
  printf("rand address: %X\n", r);

  for(a=0; a<10; a++) {
    uint16_t randomNum = read(myfile, &rand, sizeof(rand));
    printf("%u\n", rand);
  }

  close(myfile);
  return(0);

}

