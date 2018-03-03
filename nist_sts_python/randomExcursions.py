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
    x = list()             # Convert to +1,-1
    for bit in input_str:
        #if bit == 0:
        x.append((int(bit)*2)-1)

    #print "x=",x
    # Build the partial sums
    pos = 0
    s = list()
    for e in x:
        pos = pos+e
        s.append(pos)    
    sprime = [0]+s+[0] # Add 0 on each end
    
    #print "sprime=",sprime
    # Build the list of cycles
    pos = 1
    cycles = list()
    while (pos < len(sprime)):
        cycle = list()
        cycle.append(0)
        while sprime[pos]!=0:
            cycle.append(sprime[pos])
            pos += 1
        cycle.append(0)
        cycles.append(cycle)
        pos = pos + 1
    
    J = len(cycles)
    # print "J="+str(J)    
    
    vxk = [['a','b','c','d','e','f'] for y in [-4,-3,-2,-1,1,2,3,4] ]

    # Count Occurances  
    for k in xrange(6):
        for index in xrange(8):
            mapping = [-4,-3,-2,-1,1,2,3,4]
            x = mapping[index]
            cyclecount = 0
            #count how many cycles in which x occurs k times
            for cycle in cycles:
                oc = 0
                #Count how many times x occurs in the current cycle
                for pos in cycle:
                    if (pos == x):
                        oc += 1
                # If x occurs k times, increment the cycle count
                if (k < 5):
                    if oc == k:
                        cyclecount += 1
                else:
                    if k == 5:
                        if oc >=5:
                            cyclecount += 1
            vxk[index][k] = cyclecount
    
    # Table for reference random probabilities
    pixk=[[0.5     ,0.25   ,0.125  ,0.0625  ,0.0312 ,0.0312],
          [0.75    ,0.0625 ,0.0469 ,0.0352  ,0.0264 ,0.0791],
          [0.8333  ,0.0278 ,0.0231 ,0.0193  ,0.0161 ,0.0804],
          [0.875   ,0.0156 ,0.0137 ,0.012   ,0.0105 ,0.0733],
          [0.9     ,0.01   ,0.009  ,0.0081  ,0.0073 ,0.0656],
          [0.9167  ,0.0069 ,0.0064 ,0.0058  ,0.0053 ,0.0588],
          [0.9286  ,0.0051 ,0.0047 ,0.0044  ,0.0041 ,0.0531]]
    randomExcursions
    success = True
    plist = list()
    for index in xrange(8):
        mapping = [-4,-3,-2,-1,1,2,3,4]
        x = mapping[index]
        chisq = 0.0
        for k in xrange(6):
            top = float(vxk[index][k]) - (float(J) * (pixk[abs(x)-1][k]))
            top = top*top
            bottom = J * pixk[abs(x)-1][k]
            chisq += top/bottom
        p = gammaincc(5.0/2.0,chisq/2.0)
        plist.append(p)
        if p < 0.01:
            err = " Not Random"
            success = False
        else:
            err = ""
    #     print "x = %1.0f\tchisq = %f\tp = %f %s"  % (x,chisq,p,err)
    # if (J < 500):
    #     print "J too small (J < 500) for result to be reliable"
    # elif success:
    #     print "PASS"
    # else:    
    #     print "FAIL: Data not random"
    return min(plist)

def randomExcursions_all(input_str,coordinates,queue=None,func_name=None,):
    print "randomExcursions_all"
    result = []
    for coordinate in coordinates:
        p_value = randomExcursions(input_str[coordinate[0]:coordinate[1]+1])
        result.append(p_value)
    if queue!=None and func_name!=None:
        # queue.put((result,func_name))
        queue.append((result,func_name))
    print "randomExcursions_all end"
    return (result,func_name)

def main():
    input_str = open("/Users/houseyoung/TestData/data.e").read(1000000)
    # input_str = "0110110101"
    print randomExcursions(input_str)

if __name__ == '__main__':
    main()