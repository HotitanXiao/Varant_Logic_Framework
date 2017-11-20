# coding:utf-8
"""
参数: 
输出: 
描述: 
这个家伙返回两个值，
取最小的作为结果返回

首先将01序列转换为（-1，1）利用公示 2x-1进行转换
然后进行累加计算
没S有l个比特位，则计算得到l个累加和值
然后构造S' = 0，S，0，然后计算得到l+2个累加和的值

令J为S'中0得数目


"""
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include "../include/externs.h"
#include "../include/cephes.h"
from mathUtils import *
def CumulativeSums(input_str):
    """
    参数: 
    输出: 
    描述: 
    """
    S = 0
    sup = 0
    inf = 0
    sum1,sum2 = 0,0
    zrev = 0
    n = len(input_str)
    for k in xrange(0, n):
        if input_str[k] == "1":
            S += 1
        else:
            S -= 1 
        if S > sup:
            sup += 1
        if S < inf:
            inf -= 1
        z = max((sup,-inf))
        zrev = max((sup-S,S-inf))
    
    # // forward
    sum1 = 0.0
    for k in xrange(int((-n/z+1)/4),int((n/z-1)/4)+1):
        sum1 += normal(((4*k+1)*z)/math.sqrt(n));
        sum1 -= normal(((4*k-1)*z)/math.sqrt(n));

    sum2 = 0.0;
    for k in xrange(int((-n/z-3)/4),int((n/z-1)/4)+1):
        sum2 += normal(((4*k+3)*z)/math.sqrt(n));
        sum2 -= normal(((4*k+1)*z)/math.sqrt(n));


    p_value = 1.0 - sum1 + sum2;
    
    # fprintf(stats[TEST_CUSUM], "\t\t      CUMULATIVE SUMS (FORWARD) TEST\n");
    # fprintf(stats[TEST_CUSUM], "\t\t-------------------------------------------\n");
    # fprintf(stats[TEST_CUSUM], "\t\tCOMPUTATIONAL INFORMATION:\n");
    # fprintf(stats[TEST_CUSUM], "\t\t-------------------------------------------\n");
    # fprintf(stats[TEST_CUSUM], "\t\t(a) The maximum partial sum = %d\n", z);
    # fprintf(stats[TEST_CUSUM], "\t\t-------------------------------------------\n");

    # if ( isNegative(p_value) || isGreaterThanOne(p_value) )
    #     fprintf(stats[TEST_CUSUM], "\t\tWARNING:  P_VALUE IS OUT OF RANGE\n");

    # fprintf(stats[TEST_CUSUM], "%s\t\tp_value = %f\n\n", p_value < ALPHA ? "FAILURE" : "SUCCESS", p_value);
    # fprintf(results[TEST_CUSUM], "%f\n", p_value);
        
    # // backwards
    sum1 = 0.0
    for k in xrange(int((-n/zrev+1)/4),int((n/zrev-1)/4)+1):
        sum1 += normal(((4*k+1)*zrev)/math.sqrt(n));
        sum1 -= normal(((4*k-1)*zrev)/math.sqrt(n));

    sum2 = 0.0
    for k in xrange(int((-n/zrev-3)/4),int((n/zrev-1)/4)+1):
        sum2 += normal(((4*k+3)*zrev)/math.sqrt(n));
        sum2 -= normal(((4*k+1)*zrev)/math.sqrt(n));

    p_value2 = 1.0 - sum1 + sum2;

    return min(p_value,p_value2)

    # fprintf(stats[TEST_CUSUM], "\t\t      CUMULATIVE SUMS (REVERSE) TEST\n");
    # fprintf(stats[TEST_CUSUM], "\t\t-------------------------------------------\n");
    # fprintf(stats[TEST_CUSUM], "\t\tCOMPUTATIONAL INFORMATION:\n");
    # fprintf(stats[TEST_CUSUM], "\t\t-------------------------------------------\n");
    # fprintf(stats[TEST_CUSUM], "\t\t(a) The maximum partial sum = %d\n", zrev);
    # fprintf(stats[TEST_CUSUM], "\t\t-------------------------------------------\n");

    # if ( isNegative(p_value) || isGreaterThanOne(p_value) )
    #     fprintf(stats[TEST_CUSUM], "\t\tWARNING:  P_VALUE IS OUT OF RANGE\n");

    # fprintf(stats[TEST_CUSUM], "%s\t\tp_value = %f\n\n", p_value < ALPHA ? "FAILURE" : "SUCCESS", p_value); fflush(stats[TEST_CUSUM]);
    # fprintf(results[TEST_CUSUM], "%f\n", p_value); fflush(results[TEST_CUSUM]);
# def CumulativeSums_all(input_str,coordinates,queue=None,func_name=None):
#     """
#     参数: 
#     输出: 
#     描述: 
#     """
#     result = []
    
#     for coordinate in coordinates:
#         p_value = CumulativeSums(input_str[coordinate[0]:coordinate[1]+1])
#         result.append(p_value)
#     print func_name
#     if queue!=None and func_name!=None:
#         # queue.put((result,func_name))
#         queue.append((result,func_name))
#     return (result,func_name)


def main():
    a = "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"
    print CumulativeSums(a)
if __name__ == '__main__':
    main()