#include <stdio.h>
#include <stdlib.h>

#include "libmemory.h"

int main(){
  int size = 300;
  int runTime = 10;
  printf("hello\n");
  struct Block *blocks = occupy(size);
  sleep(runTime);
  free(blocks);
}
