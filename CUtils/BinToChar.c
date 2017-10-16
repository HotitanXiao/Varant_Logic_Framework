/*
	Date: 2017-4-25
    Author:H.Y
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUFFER_SIZE 4096
#define KEYBUFFER_SIZE 512
#define MAX_KEY_SIZE 8

int ConvertByteToBinary(unsigned char *keybuffer, char *strbuffer, int keyslength, int keysize)
{
    /*
        参数：keybuffer(读取的数据),strbuffer(存放转换结果的内存), keyslength(读取数据量),keysize(单个区域的bit数量)
    */
	unsigned char flag = 0x01;
	int i, j;
	for (i = 0; i < keyslength && i < KEYBUFFER_SIZE; i++)
	{
		flag = 0x01;
		for (j = 0; j < keysize && j < MAX_KEY_SIZE; j++)
		{
			if (flag & keybuffer[i])
				strbuffer[keysize * i + keysize - 1 - j] = '1';
			else
				strbuffer[keysize * i + keysize - 1 - j] = '0';
			flag = flag << 1;
		}
	}
	return 0;
}

int FileBinToChar(char *filename, char *outfilename)
{
    /*
        参数：filename(输入文件路径),outfilename(输出文件路径)
    */

	int keysize = 8;
	int keyslength = BUFFER_SIZE / keysize;
	int readlength = 0;
	errno_t err;
	char *strbuffer = (char *)malloc(4096 * sizeof(char));
	unsigned char *keybuffer = (unsigned char *)malloc(keyslength * sizeof(char));
	FILE *file = NULL;
	FILE *outfile = NULL;

	file = fopen(filename, "rb");
	outfile = fopen(outfilename, "wb");
    if (file==NULL)
    {
        printf("input file -%s- open error",filename);
        return 0;
    }
    if(outfile == NULL){
        printf("output file --%s-- open error",outfilename);
        return 0;
    }
	while ((readlength = fread(keybuffer, keysize/8, KEYBUFFER_SIZE, file)) > 0)
	{
		ConvertByteToBinary(keybuffer, strbuffer, readlength, keysize);
		fwrite(strbuffer, 1, readlength*keysize, outfile);
	}
	fclose(outfile);

	return 0;
}

int CreateZeroFile(char *outfilename,int filesize)
{
    /*
        参数:filesize(文件的byte大小),outfilename(输出文件路径)
    */
    int loopRound = 0;
    int i = 0;
    int leftByte = 0;
    FILE* outfile = NULL;
    loopRound = filesize / KEYBUFFER_SIZE; leftByte = filesize % KEYBUFFER_SIZE;
    outfile = fopen(outfilename,"wb");
    if(outfile == NULL)
    {
        printf("output file open error");
        return 0;
    }

    char * outStreamBuffer = (char *)malloc(4096*sizeof(char));
    for(i=0; i<loopRound;i++)
    {
        fwrite(outStreamBuffer,sizeof(char),4096,outfile);
    }
    if(leftByte){ fwrite(outStreamBuffer,sizeof(char),leftByte,outfile); }
    fclose(outfile);
	return 0;
}

int main(int argc, char **argv)
{
    /*
        argv：-Z（生成全0的数据）outfilename size(byte), -C（进行转换）infilename outfilename
    */
	if (argc >1)
	{
        if(strcmp(argv[1],"-C")==0 && argc==4)
		{
			char *filename = argv[2];
			char *outfilename = argv[3];
			strcpy(outfilename,filename);
			strcat(outfilename, ".char");
			FileBinToChar(filename, outfilename);
		}else if (strcmp(argv[1],"-Z")==0 && argc==4)
		{	
			int filesize = atoi(argv[3]);
			CreateZeroFile(argv[2],filesize);
		}
		
	}
	else
	{
		printf("params errors %d \n", argc);
	}
	return 0;
}