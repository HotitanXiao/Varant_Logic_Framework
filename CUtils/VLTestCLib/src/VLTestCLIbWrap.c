
/*
	Author: H.Y
	FileName:
	Date: 2018-04-14
	Description:本文件是为Python提供Api的
*/
#include"VLTestClib.h"
#include<Python.h>


static PyObject * PyVLTestForChar(PyObject* self, PyObject* args, PyObject *keywords)
{
	//需要得参数就是字符串
	//还有m值
	int m=0,i=0;

	char * inputStr = "";
	static char *kwlist[] = { "input_str", "m", NULL };
	int *qArray = NULL;
	int *pArray = NULL;
	int segmentCount = 0;

	if (!PyArg_ParseTupleAndKeywords(args, keywords, "s|i", kwlist,
		&inputStr, &m))
		return Py_None;
	printf("length of input string that as input of VLCLib is %d \n", strlen(inputStr));
	
	//根据输入的字符串长度来判断了
	segmentCount = strlen(inputStr) / m;
	printf("segment is %d \n", segmentCount);
	pArray = malloc(segmentCount*sizeof(int));
	qArray = malloc(segmentCount*sizeof(int));
	memset(pArray, 0, segmentCount*sizeof(int));
	memset(qArray, 0, segmentCount * sizeof(int));

	printf("malloc complete \n");
 	VLTestForChar(inputStr, strlen(inputStr), m, pArray, segmentCount, qArray, segmentCount);
	printf("Analyze complete \n");
	PyObject * pResultList = PyList_New(segmentCount);
	PyObject * qResultList = PyList_New(segmentCount);
	for (i = 0; i < segmentCount; i++) 
	{
		PyList_SetItem(pResultList, i, PyInt_FromLong(*(pArray+i)));
		//printf("p = %d\n", *(pArray + i));
		PyList_SetItem(qResultList, i, PyInt_FromLong(*(qArray + i)));
		//printf("q = %d\n", *(pArray + i));

	}
	printf("Array to PyObject complete %d \n",PyList_Size(pResultList));
	PyObject *resultTuple = PyTuple_New(2);
	PyTuple_SetItem(resultTuple, 0, pResultList);
	PyTuple_SetItem(resultTuple, 1, qResultList);
	return resultTuple;
}

static PyMethodDef VLTestMethods[] = {
	{"PyVLTestForChar",  (PyCFunction)PyVLTestForChar, METH_KEYWORDS,
		"Get VL Feature With C Language"},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};


PyMODINIT_FUNC initVLTest(void)
{
	(void)Py_InitModule("VLTest", VLTestMethods);
}

int main(int argc, char *argv[])
{
	Py_SetProgramName(argv[0]);

	/* Initialize the Python interpreter.  Required. */
	Py_Initialize();

	/* Add a static module */
	initVLTest();


}