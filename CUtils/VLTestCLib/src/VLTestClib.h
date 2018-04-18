#pragma once
//#include<Python.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

void VLTestForChar(char* inputStr, int inputStrLen, int m, int* pArrayCache, int pArraySize, int* qArrayCache, int qArraySize);
void VLTowStringXorForChar(char* string1, int len1, char* string2, int len2);