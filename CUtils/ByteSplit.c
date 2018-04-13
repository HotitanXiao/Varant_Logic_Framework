// 本方法是用来对一个文本文件进行8bit的分割的，一个byte的8个bit被分割到不同的文件当中去
#include<stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUFFER_SIZE 4096
#define KEYBUFFER_SIZE 512
#define MAX_KEY_SIZE 8


void ByteSplit(char * filename){
    char filenameTemp[256] = {0}; //用于临时存放文件路径的
    int readLength = 0;
    int x,y = 0;
    // 对文本内容进行相应的拆分的
    printf("Doing\n");
    FILE * inputFile = fopen(filename,"rb");
    if (inputFile == NULL){
        printf("ERROR: cannot open the input file\n");
    }
    printf("open input file  complete\n");
    // 读取数据的缓冲区
    unsigned char* input_cache = malloc(8*BUFFER_SIZE*sizeof(char));
    // // 申请8个长度为4096大小的内存空间
    unsigned char* file0_cache = malloc(BUFFER_SIZE*sizeof(char));
    unsigned char* file1_cache = malloc(BUFFER_SIZE*sizeof(char));
    unsigned char* file2_cache = malloc(BUFFER_SIZE*sizeof(char));
    unsigned char* file3_cache = malloc(BUFFER_SIZE*sizeof(char));
    unsigned char* file4_cache = malloc(BUFFER_SIZE*sizeof(char));
    unsigned char* file5_cache = malloc(BUFFER_SIZE*sizeof(char));
    unsigned char* file6_cache = malloc(BUFFER_SIZE*sizeof(char));
    unsigned char* file7_cache = malloc(BUFFER_SIZE*sizeof(char));


    if( file0_cache==NULL ||
        file1_cache==NULL ||
        file2_cache==NULL ||
        file3_cache==NULL ||
        file4_cache==NULL ||
        file5_cache==NULL ||
        file6_cache==NULL ||
        file7_cache==NULL)
        {
            printf("ERROR: cannot malloc enougth memory for file cache");
        }
    printf("malloc complete,start open file\n");
    // // 开始打开待存储的文件
    strcpy(filenameTemp,filename);
    char * filename0 = strcat(filenameTemp,".split0");
    FILE * file0 = fopen(filename0,"wba");
    printf("open %s complete\n",filenameTemp);
    
    strcpy(filenameTemp,filename);
    char * filename1 = strcat(filenameTemp,".split1");
    FILE * file1 = fopen(filename1,"wba");

    strcpy(filenameTemp,filename);
    char * filename2 = strcat(filenameTemp,".split2");
    FILE * file2 = fopen(filename2,"wba");

    strcpy(filenameTemp,filename);
    char * filename3 = strcat(filenameTemp,".split3");
    FILE * file3 = fopen(filename3,"wba");

    strcpy(filenameTemp,filename);
    char * filename4 = strcat(filenameTemp,".split4");
    FILE * file4 = fopen(filename4,"wba");

    strcpy(filenameTemp,filename);
    char * filename5 = strcat(filenameTemp,".split5");
    FILE * file5 = fopen(filename5,"wba");

    strcpy(filenameTemp,filename);
    char * filename6 = strcat(filenameTemp,".split6");
    FILE * file6 = fopen(filename6,"wba");

    strcpy(filenameTemp,filename);
    char * filename7 = strcat(filenameTemp,".split7");
    FILE * file7 = fopen(filename7,"wba");
    printf("open file complte");

    readLength = fread(input_cache,1,8*BUFFER_SIZE*sizeof(char),inputFile);
    while(readLength!=0){
        printf("read length=%d",readLength);
        for(x = 0;x<readLength/8;x++){
            file0_cache[x] = input_cache[x*8];
            file1_cache[x] = input_cache[x*8+1];
            file2_cache[x] = input_cache[x*8+2];
            file3_cache[x] = input_cache[x*8+3];
            file4_cache[x] = input_cache[x*8+4];
            file5_cache[x] = input_cache[x*8+5];
            file6_cache[x] = input_cache[x*8+6];
            file7_cache[x] = input_cache[x*8+7];
        }
        fwrite(file0_cache,BUFFER_SIZE*sizeof(char),1,file0);
        fwrite(file1_cache,BUFFER_SIZE*sizeof(char),1,file1);
        fwrite(file2_cache,BUFFER_SIZE*sizeof(char),1,file2);
        fwrite(file3_cache,BUFFER_SIZE*sizeof(char),1,file3);
        fwrite(file4_cache,BUFFER_SIZE*sizeof(char),1,file4);
        fwrite(file5_cache,BUFFER_SIZE*sizeof(char),1,file5);
        fwrite(file6_cache,BUFFER_SIZE*sizeof(char),1,file6);
        fwrite(file7_cache,BUFFER_SIZE*sizeof(char),1,file7);
        readLength = fread(input_cache,1,8*BUFFER_SIZE*sizeof(char),inputFile);
    }


    fclose(file0);
    fclose(file1);
    fclose(file2);
    fclose(file3);
    fclose(file4);
    fclose(file5);
    fclose(file6);
    fclose(file7);


}
int main(int argc, char **argv)
{
    /*
        argv：-Z（生成全0的数据）outfilename size(byte), -C（进行转换）infilename outfilename
    */
	if (argc >1)
	{
        if(strcmp(argv[1],"-S")==0 && argc==3)
		{
			char *filename = argv[2];
			ByteSplit(filename);
		}else{
            printf("param errors\n");
        }
		
	}
	else
	{
		printf("params errors %d \n", argc);
	}
	return 0;
}