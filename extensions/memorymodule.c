#include <Python.h>

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

  char message[100];
  sprintf(message, "Started memory run.\n");
  quick_log(message);

  struct Block *blocks = malloc(totalBlocks * sizeof(struct Block));
  int i;
  for (i = 0; i<totalBlocks; ++i){
    blocks[i].data = malloc(blockSize);
    int j;
    for (j=0; j<numberInts; j++)
      blocks[i].data[j] = j;
  }

  sprintf(message, "Reserved %d blocks of 1 MB (%d bytes). %d MB total.\n", size, (int) blockSize, size*(int)blockSize);
  quick_log(message);

  return blocks;
}

// module functions
//------------------

static PyObject*
memory_run(PyObject *self, PyObject *args){
  const int size;
  const int runTime;

  if (!PyArg_ParseTuple(args, "ii", &size, &runTime))
    return NULL;
  struct Block *blocks = occupy(size);
  sleep(runTime);
  free(blocks);

  int result_code = 1;
  return Py_BuildValue("i", result_code);

  Py_RETURN_NONE;
}

// Python interface declaration
//-------------------------------

static PyMethodDef MemoryMethods[] = {
    {"run",  memory_run, METH_VARARGS,
     "Occupy some memory."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC
initmemory(void)
{
    (void) Py_InitModule("memory", MemoryMethods);
}
