// helper functions
//-----------------

struct Block{
  int *data;
};

void quick_log(char *message){
  printf("%s", message);
  }

struct Block* occupy(int size){
  // we will divide it up into 1 MB blocks to be able to address them
  unsigned long blockSize = 1024*1024; // bytes
  unsigned long totalBlocks = size;
  // inside each block occupy an int array of blockSize bytes
  unsigned long numberInts = blockSize/sizeof(int);

  struct Block *blocks = malloc(totalBlocks * sizeof(struct Block));
  int i;
  for (i = 0; i<totalBlocks; ++i){
    blocks[i].data = malloc(blockSize);
    int j;
    for (j=0; j<numberInts; j++)
      blocks[i].data[j] = j;
  }
    
  char message[50];
  sprintf(message, "Reserved %d blocks of 1 MB (%d bytes). %d MB total.\n", size, (int) blockSize, size*(int)blockSize);
  quick_log(message);

  return blocks;
}
