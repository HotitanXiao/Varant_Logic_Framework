# coding:utf-8
"""
作者: H.Y
日期: 
描述: 
Maurer’s “Universal Statistical” Test
The focus of this test is the number of bits between matching patterns 
(a measure that is related to the length of a compressed sequence).
 The purpose of the test is to detect whether or not the sequence can be significantly compressed without loss of information. A significantly compressible sequence is considered to be non-random.
该检测方法的目标是 mathch patterns 之间的比特数目
和压缩序列的长度有关
检测的大致方法是检测是否可以无损压缩
无损压缩的就是非随机的
"""

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include "../include/externs.h"
#include "../include/utilities.h"
#include "../include/cephes.h"

# /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#                          U N I V E R S A L  T E S T
#  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
import math


def universal(input_str):
    decRep = 0
    expected_value = [0, 0, 0, 0, 0, 0, 5.2177052, 6.1962507, 7.1836656,
                8.1764248, 9.1723243, 10.170032, 11.168765,
                12.168070, 13.167693, 14.167488, 15.167379 ]
    variance = [ 0, 0, 0, 0, 0, 0, 2.954, 3.125, 3.238, 3.311, 3.356, 3.384,
                3.401, 3.410, 3.416, 3.419, 3.421 ]
    n = len(input_str)
    
    # /* * * * * * * * * ** * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    #  * THE FOLLOWING REDEFINES L, SHOULD THE CONDITION:     n >= 1010*2^L*L       *
    #  * NOT BE MET, FOR THE BLOCK LENGTH L.                                        *
    #  * * * * * * * * * * ** * * * * * * * * * * * * * * * * * * * * * * * * * * * */
    L = 5
    if n >= 387840:
        L = 6
    if n >= 904960:
        L = 7
    if n >= 2068480:
        L = 8
    if n >= 4654080:
        L = 9
    if n >= 10342400:
        L = 10
    if n >= 22753280:
        L = 11
    if n >= 49643520:
        L = 12
    if n >= 107560960:
        L = 13
    if n >= 231669760:
        L = 14
    if n >= 496435200:
        L = 15
    if n >= 1059061760:
        L = 16
    
    Q = 10*pow(2, L)
    K = int(math.floor(n/L) - Q	 )		    #/* BLOCKS TO TEST */
    
    p = pow(2, L)
    T = [0]*p
    # if ( (L < 6) || (L > 16) || ((double)Q < 10*pow(2, L)) ||
    #      ((T = (long *)calloc(p, sizeof(long))) == NULL) ) {
    #     print "\t\tUNIVERSAL STATISTICAL TEST\n"
    #     print "\t\t---------------------------------------------\n"
    #     print "\t\tERROR:  L IS OUT OF RANGE.\n"
    #     print "\t\t-OR- :  Q IS LESS THAN %s\n" % 10*pow(2, L)
    #     print "\t\t-OR- :  Unable to allocate T.\n"
    #     return
    # }
    
    # /* COMPUTE THE EXPECTED:  Formula 16, in Marsaglia's Paper */
    c = 0.7 - 0.8/L + (4 + 32/L)*pow(K, -3/L)/15
    sigma = c * math.sqrt(variance[L]/K)
    sqrt2 = math.sqrt(2)
    sum = 0.0
    for i in range(0,p):
        T[i] = 0
    # /* INITIALIZE TABLE */
    for i in xrange(1,Q+1):
        decRep = 0
        for j in xrange(0,L):
            decRep += int(input_str[(i-1)*L+j]) * pow(2, L-1-j)		
        T[decRep] = i
    # /* PROCESS BLOCKS */
    for i in xrange(Q+1,Q+K+1):
        decRep = 0  
        for j in xrange(0,L):
            decRep += int(input_str[(i-1)*L+j]) * pow(2, L-1-j)
        sum += math.log(i - T[decRep])/math.log(2)
        T[decRep] = i

    phi = sum/K
    arg = math.fabs(phi-expected_value[L])/(sqrt2 * sigma)
    p_value = math.erfc(arg)
    return p_value
    # fprintf(stats[TEST_UNIVERSAL], "\t\tUNIVERSAL STATISTICAL TEST\n")
    # fprintf(stats[TEST_UNIVERSAL], "\t\t--------------------------------------------\n")
    # fprintf(stats[TEST_UNIVERSAL], "\t\tCOMPUTATIONAL INFORMATION:\n")
    # fprintf(stats[TEST_UNIVERSAL], "\t\t--------------------------------------------\n")
    # fprintf(stats[TEST_UNIVERSAL], "\t\t(a) L         = %d\n", L)
    # fprintf(stats[TEST_UNIVERSAL], "\t\t(b) Q         = %d\n", Q)
    # fprintf(stats[TEST_UNIVERSAL], "\t\t(c) K         = %d\n", K)
    # fprintf(stats[TEST_UNIVERSAL], "\t\t(d) sum       = %f\n", sum)
    # fprintf(stats[TEST_UNIVERSAL], "\t\t(e) sigma     = %f\n", sigma)
    # fprintf(stats[TEST_UNIVERSAL], "\t\t(f) variance  = %f\n", variance[L])
    # fprintf(stats[TEST_UNIVERSAL], "\t\t(g) exp_value = %f\n", expected_value[L])
    # fprintf(stats[TEST_UNIVERSAL], "\t\t(h) phi       = %f\n", phi)
    # fprintf(stats[TEST_UNIVERSAL], "\t\t(i) WARNING:  %d bits were discarded.\n", n-(Q+K)*L)
    # fprintf(stats[TEST_UNIVERSAL], "\t\t-----------------------------------------\n")

def universal_all(input_str,coordinates,input_dict=None):
    """
    参数: N=8，m=4
    输出: 
    描述: 
    """ 
    result = []
    for coordinate in coordinates:
        p_value = universal(input_str)
        result.append(p_value)
    if input_dict:
        input_dict["cache"] = result
    return result

def main():
    input_str = open("../TestData/data.sha1.char","rb").read()
    print len(input_str)
    print universal(input_str)

if __name__ == '__main__':
    main()