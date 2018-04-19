# coding:utf-8
"""
Author: H.Y
FileName: ByteSplit
Date: 2018-04-12
Descripthon: 对一个byte进行分割，分割成为8个文件，一个byte包含8个bit
            将每个bit分割到不同的8个文件当中。产生对应bit值的序列
"""

def byte_split(file_name):
    """
    Author: H.Y
    Date: 
    Params: 
    Descripthon: 
    """
    input_str = open(file_name,"rb").read(10000000)
    bits_set = ["" for x in xrange(0,8)]
    file_set = [open(file_name+".split-%s" % x,"wb") for x in range(0,8)]
    for x in xrange(0,len(input_str)/8):
        for y in xrange(0,8):
            bits_set[y]+= input_str[x*8+y]
    
    for t in xrange(0,8):
        file_set[t].write(bits_set[t])
        file_set[t].close()

def main():
    input_file = open("/Users/houseyoung/TestData/vrc4_std.char.split7")
    input_str = input_file.read(100000)
    print input_str
    # while len(input_str)!=None:
    #     if len(input_str)<100000:
    #         print input_str
    #     input_str = input_file.read(100000)

if __name__ == '__main__':
    main()