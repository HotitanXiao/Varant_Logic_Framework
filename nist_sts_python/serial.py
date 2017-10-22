# coding:utf-8
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include "../include/externs.h"
#include "../include/cephes.h"  

from mathUtils import *

def serial(input_str,m):
    """
    参数: 
    输出: 
    描述:
        序列检测 
        这里会产生两个p_value的值
    """
    n = len(input_str)
    psim0 = psi2(input_str,m, n);
    psim1 = psi2(input_str,m-1, n);
    psim2 = psi2(input_str,m-2, n);
    del1 = psim0 - psim1;
    del2 = psim0 - 2.0*psim1 + psim2
    p_value1 = igamc(pow(2, m-1)/2, del1/2.0)
    p_value2 = igamc(pow(2, m-2)/2, del2/2.0)

    # return p_value1,p_value2
    return min(p_value1,p_value2)


def psi2(input_str,m,n):
    """
    参数: 
    输出: 
    描述: 
    """
    n = len(input_str)
    i, j, k, powLen = (0,0,0,0)
    all_sum = 0.0
    numOfBlocks = n

    powLen = int(pow(2,m+1)-1)
    P = [0] * powLen
    if ( (m == 0) or (m == -1) ):
        return 0.0
    numOfBlocks = n;

    for i in xrange(0,numOfBlocks):
        k = 1;
        for j in xrange(0,m):
            if input_str[(i+j)%n] == "0":
                k *= 2
            elif input_str[(i+j)%n] == "1":
                k = 2*k + 1 
        P[k-1] += 1
    all_sum = 0.0;
    for i in xrange(int(pow(2,m)-1), int(pow(2,m+1)-1)):
        all_sum += pow(P[i], 2)
    all_sum = (all_sum * pow(2, m)/n) - n

    return all_sum


def serial_all(input_str,coordinates,input_queue=None,func_name=None):
    """
    参数: 
    输出: 
    描述: 
    默认调用serial的m为8，不知道大点有没有效果
    """
    result = []
    for coordinate in coordinates:
        p_value = serial(input_str[coordinate[0]:coordinate[1]+1],8)
        result.append(p_value)
    if input_queue and func_name:
        input_queue.put((result,func_name))
    return result



def main():
    input_str = open("../TestData/data.e").read(100000)
    print serial(input_str,16)

if __name__ == '__main__':
    main()