#include <Python.h>

static PyObject*
memory_run(PyObject *self, PyObject *args){
  const int *size;

  if (!PyArg_ParseTuple(args, "i", &size))
    return NULL;
  
  int *a = malloc(sizeof(int)*(*size));
  int i;
  for (i=0; i<*size; i++)
    a[i] = i;
  sleep(1);

  int result_code = 1;
  return Py_BuildValue("i", result_code);
}
