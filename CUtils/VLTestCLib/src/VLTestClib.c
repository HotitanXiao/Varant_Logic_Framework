#include"VLTestClib.h"
/*
	Author: H.Y
	Date:�ļ�ͷ��Ȩ��Ϣ
	Input:
	Output:
	Description:����
*/

void VLTestForChar(char* inputStr,int inputStrLen,int m, int* pArrayCache, int pArraySize,int* qArrayCache,int qArraySize)
{
	
	int i, j, k = 0;
	int p=0, q=0,offset = 0;
	int pArrayCacheIndex = 0;
	int qArrayCacheIndex = 0;
	char *flag = inputStr;//ȫ�ֵ�ָ�룬
	char *innerFlag = inputStr;
	//int �Զ�����ȡ����
	for (i = 0; i < inputStrLen / m && pArrayCacheIndex< qArraySize && qArrayCacheIndex < qArraySize; i++) {
		for (j = 0; j < m; j++) {
			switch (*(flag+m*i+j))
			{
			case '1':
				p += 1;
				// �ж�ǰ��һ���ǲ���0
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
		//��¼��ȥ
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



/*
	Author: H.Y
	Date: 2018-04-15
	Input: �����ַ���������
	Output: �����
	Description:��������
*/

void VLTowStringXorForChar(char* string1,int len1, char* string2,int len2)
{
	int index = 0;
	if (len1==0||
		len2 == 0||
		len1 != len2)
		return;
	else 
	{
		for (index = 0; index < len1; index++)
		{
			*(string1 + index) = *(string1 + index) == *(string2 + index) ? '0' : '1';
		}
	}
}