#include"VLTestClib.h"
/*
	Author: H.Y
	Date:文件头版权信息
	Input:
	Output:
	Description:描述
*/

void VLTestForChar(char* inputStr,int inputStrLen,int m, int* pArrayCache, int pArraySize,int* qArrayCache,int qArraySize)
{
	
	int i, j, k = 0;
	int p=0, q=0,offset = 0;
	int pArrayCacheIndex = 0;
	int qArrayCacheIndex = 0;
	char *flag = inputStr;//全局的指针，
	char *innerFlag = inputStr;
	//int 自动向下取整了
	for (i = 0; i < inputStrLen / m && pArrayCacheIndex< qArraySize && qArrayCacheIndex < qArraySize; i++) {
		for (j = 0; j < m; j++) {
			switch (*(flag+m*i+j))
			{
			case '1':
				p += 1;
				// 判断前面一个是不是0
				if (j == 0) {
					offset = m - 1;
				}
				else
					offset = j-1;
				if (flag[m*i + offset] == '0')
					q += 1;
			default:
				continue;
			}
		}
		//记录进去
		*(pArrayCache+pArrayCacheIndex) = p;
		*(qArrayCache+qArrayCacheIndex) = q;
		p=0, q = 0;
		pArrayCacheIndex++;
		qArrayCacheIndex++;
	}
}

void VLTestForInt(char* inputStr, int m, int* pArrayCache, int* qArrayCache)
{

}