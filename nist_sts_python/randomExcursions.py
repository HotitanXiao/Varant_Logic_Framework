# coding:utf-8
"""
作者: H.Y
日期: 
描述: 
随机偏移检测

基础的计算和cusum一样
然后是寻找cycle的不过程了
"""
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include "../include/externs.h"
#include "../include/cephes.h"  
import math
from mathUtils import *

def randomExcursions(input_str):
    """
    参数: 
    输出: 
    描述: 

    """
    n = len(input_str)

    cycleStart = 0
    cycleStop = 0
    cycle = [0] * max(1000, int(n/100))
    S_k = [0] * n
    stateX = [ -4, -3, -2, -1, 1, 2, 3, 4 ]
    counter = [ 0, 0, 0, 0, 0, 0, 0, 0]

    nu = [[0]*8]*6 
    pi = [ [0.0000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.0000000000], 
                         [0.5000000000, 0.25000000000, 0.12500000000, 0.06250000000, 0.03125000000, 0.0312500000],
                         [0.7500000000, 0.06250000000, 0.04687500000, 0.03515625000, 0.02636718750, 0.0791015625],
                         [0.8333333333, 0.02777777778, 0.02314814815, 0.01929012346, 0.01607510288, 0.0803755143],
                         [0.8750000000, 0.01562500000, 0.01367187500, 0.01196289063, 0.01046752930, 0.0732727051] ]
    
    J = 0
    S_k[0] = 2*int(input_str[0]) -1
    for i in xrange(1,n):
        S_k[i] = S_k[i-1] + 2*int(input_str[i]) - 1
        if S_k[i] == 0:
            J += 1
            if J > max(1000,n/100):
                print "ERROR IN FUNCTION randomExcursions:  EXCEEDING THE MAX NUMBER OF CYCLES EXPECTED\n."
                return 0
            cycle[J] = i
    if S_k[n-1] != 0:
        J += 1
    
    cycle[J] = n
    # print cycle

    # fprintf(stats[TEST_RND_EXCURSION], "\t\t\t  RANDOM EXCURSIONS TEST\n");
    # fprintf(stats[TEST_RND_EXCURSION], "\t\t--------------------------------------------\n");
    # fprintf(stats[TEST_RND_EXCURSION], "\t\tCOMPUTATIONAL INFORMATION:\n");
    # fprintf(stats[TEST_RND_EXCURSION], "\t\t--------------------------------------------\n");
    # fprintf(stats[TEST_RND_EXCURSION], "\t\t(a) Number Of Cycles (J) = %04d\n", J);
    # fprintf(stats[TEST_RND_EXCURSION], "\t\t(b) Sequence Length (n)  = %d\n", n);

    constraint = max(0.005*pow(n, 0.5), 500);

    if J < constraint:
        print "\t\t---------------------------------------------\n"
        print "\t\tWARNING:  TEST NOT APPLICABLE.  THERE ARE AN\n"
        print "\t\t\t  INSUFFICIENT NUMBER OF CYCLES.\n"
        print "\t\t---------------------------------------------\n"
        for i in xrange(0, 8):
            print  "%f\n" % 0.0
        return 

    else:

        cycleStart = 0
        cycleStop  = cycle[1]
        for k in xrange(0,6):
            for i in xrange(0,8):
                nu[k][i] = 0.
        for j in xrange(1,J+1):
            for i in xrange(0,8):
                counter[i] = 0
            for i in xrange(cycleStart,cycleStop):
                if (S_k[i] >= 1 and S_k[i] <=4 ) or (S_k[i] >= -4 and S_k[i] <= -1):
                    if S_k[i] < 0:
                        b = 4
                    else:
                        b = 3
                    counter[S_k[i]+b] += 1

            cycleStart = cycle[j] + 1
            if j < J:
                cycleStop = cycle[j+1]
            for i in xrange(0,8):
                # print counter
                if counter[i] >= 0 and counter[i]<=4:
                    nu[counter[i]][i] += 1
                elif counter[i] >= 5:
                    nu[5][i] += 1
                # print nu
        for i in xrange(0,8):
            x = stateX[i]
            all_sum = 0
            for k in xrange(0,6):
                all_sum += pow(nu[k][i] - J*pi[int(math.fabs(x))][k],2) / (J*pi[int(math.fabs(x))][k])
            p_value = igamc(2.5, all_sum/2.0)
            print p_value,all_sum

def main():
    input_str = open("../TestData/data.e").read(1000000)
    randomExcursions(input_str)

if __name__ == '__main__':
    main()