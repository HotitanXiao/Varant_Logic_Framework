
/*
	Author: H.Y
	FileName:
	Date: 2018-04-14
	Description:本文件是为Python提供Api的
*/
#include"VLTestClib.h"
#include<Python.h>


/*
	Author: H.Y
	Date: 2018-04-15
	Input: input_str1 input_str2,m
	Output: 返回变值统计结果
	Description:对两个输入文件进行异或处理后返回变值特征
*/

static PyObject * PyVLTowStringXorForChar(PyObject* self, PyObject* args, PyObject *keywords)
{
	int m = 0, i = 0;

	char * inputStr1 = "";
	char * inputStr2 = "";
	static char *kwlist[] = { "input_str1","input_str2", "m", NULL };
	int *qArray = NULL;
	int *pArray = NULL;
	int segmentCount = 0;
	int testLen = 0;
	if (!PyArg_ParseTupleAndKeywords(args, keywords, "ss|i", kwlist,
		&inputStr1,&inputStr2, &m))
		return Py_None;
	//根据输入的字符串长度来判断了
	testLen = strlen(inputStr1);
	segmentCount = strlen(inputStr1) / m;
	//printf("input_str1=%s\n len=%d", inputStr1,testLen);
	//printf("input_str2=%s\n", inputStr2);
	printf("segment is %d \n", segmentCount);
	pArray = malloc(segmentCount * sizeof(int));
	qArray = malloc(segmentCount * sizeof(int));

	char* testStrCache = (char *)malloc(testLen * sizeof(char) + 10);
	memset(testStrCache, 0, testLen);
	strncpy_s(testStrCache, testLen * sizeof(char) + 10, inputStr1, testLen * sizeof(char));
	VLTowStringXorForChar(testStrCache, testLen, inputStr2, testLen);
	//printf("xor_str = %s\n len=%d", testStrCache,strlen(testStrCache));
	printf("malloc complete \n");
	VLTestForChar(testStrCache, strlen(testStrCache), m, pArray, segmentCount, qArray, segmentCount);
	printf("Analyze complete \n");

	PyObject * pResultList = PyList_New(segmentCount);
	PyObject * qResultList = PyList_New(segmentCount);
	for (i = 0; i < segmentCount; i++)
	{
		PyList_SetItem(pResultList, i, PyInt_FromLong(*(pArray + i)));
		//printf("p = %d\n", *(pArray + i));
		PyList_SetItem(qResultList, i, PyInt_FromLong(*(qArray + i)));
		//printf("q = %d\n", *(pArray + i));
	}
	printf("Array to PyObject complete %d \n", PyList_Size(pResultList));
	PyObject *resultTuple = PyTuple_New(2);
	PyTuple_SetItem(resultTuple, 0, pResultList);
	PyTuple_SetItem(resultTuple, 1, qResultList);
	free(pArray);
	free(qArray);
	free(testStrCache);
	return resultTuple;
}

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
	free(pArray);
	free(qArray);
	return resultTuple;
}

static PyMethodDef VLTestMethods[] = {
	{"PyVLTestForChar",  (PyCFunction)PyVLTestForChar, METH_KEYWORDS,
		"Get VL Feature With C Language"},
	{ "PyVLTowStringXorForChar",  (PyCFunction)PyVLTowStringXorForChar, METH_KEYWORDS,
	"Get VL Feature For xor results of two string With C Language" },
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