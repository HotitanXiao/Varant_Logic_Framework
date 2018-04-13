# coding:utf-8
"""
参数: 
输出: 
描述: 
近似熵检测
"""
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include "../include/externs.h"
#include "../include/utilities.h"
#include "../include/cephes.h"  
import math
from mathUtils import *
def approximateEntropy(intput_str,m=6):
    seqLength = len(intput_str)		
    index = 0
    ApEn = [0] * 2
    r = 0
    
    for blockSize in (m, m+1):
        if blockSize == 0:
            ApEn[0] = 0.0
            r += 1
        else:
            numOfBlocks = float(seqLength)
            powLen = int(pow(2,blockSize+1)) - 1
            P = [0] * powLen

            for i in xrange(0,int(numOfBlocks)):
                k = 1
                for j in xrange(0, blockSize):
                    k <<= 1
                    if int(intput_str[(i+j) % seqLength]) == 1:
                        k += 1
                P[k-1] += 1
            all_sum = .0
            index =  pow(2,blockSize) -1
            for i in xrange(0,int(pow(2,blockSize))):
                if P[index] > 0:
                    all_sum += P[index] * math.log(P[index]/numOfBlocks)
                index += 1
            all_sum /= numOfBlocks
            # print blockSize,r
            ApEn[r] = all_sum
            r += 1

    apen = ApEn[0] - ApEn[1];
    
    chi_squared = 2.0*seqLength*(math.log(2) - apen);
    p_value = igamc(pow(2, m-1), chi_squared/2.0);
    
    return p_value


def approximateEntropy_all(input_str,coordinates,queue=None,func_name=None,m=6):
    print "approximateEntropy_all"
    result = []
    for coordinate in coordinates:
        p_value = approximateEntropy(input_str[coordinate[0]:coordinate[1]+1],m)
        result.append(p_value)
    if queue!=None and func_name!=None:
        # queue.put((result,func_name))
        queue.append((result,func_name))
    print "approximateEntropy_all end"
    return (result,func_name)



def main():
    a = "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"
    print approximateEntropy(a,2)


if __name__ == '__main__':
    main()