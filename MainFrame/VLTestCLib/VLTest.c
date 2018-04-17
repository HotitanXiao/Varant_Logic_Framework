#include<Python.h>
#include<std>

static PyObject* spanm_system(PyObject *self,PyObject *args)
{
    const char *commmand;
    int sts;

    return Py_BuildValue("i",sts);
}