# coding:utf-8
"""
作者: H.Y
日期: 
描述: 
线性复杂度计算
关键点是一个线性反馈移位寄存器
The purpose of this test is to determine whether or not the sequence is complex enough to be considered random. 

Random sequences are characterized by longer LFSRs. An LFSR that is too short implies non-randomness.
随机序列由较长的LFSRs产生。段的LFSR会包含非随机数
"""
import math
from mathUtils import *
import numpy as np

def linearComplexity(input_str,M):
    """
    参数: 
    输出: 
    描述: 
    """

    # i, ii, j, d, N, L, m, N_, parity, sign, 
    K = 6;
    p_value = 0
    T_ = 0
    mean = 0
    chi2 = 0
    pi = [ 0.01047, 0.03125, 0.12500, 0.50000, 0.25000, 0.06250, 0.020833]
    n = len(input_str)
    nu = [0.] * 7 
    N = int(math.floor(n/M));
    T = [0] * M
    P = [0] * M
    B_ = [0] * M
    C = [0] * M


    for ii in xrange(0,N):
        T = [0] * M
        P = [0] * M
        B_ = [0] * M
        C = [0] * M

        L = 0;
        # m is the number of iterations since L, B(x), and b were updated and initialized to 1.
        m = -1;
        d = 0;
        C[0] = 1;
        # b is a copy of the last discrepancy d (explained below) since L was updated and initialized to 1.
        # B(x) is a copy of the last C(x) since L was updated and initialized to 1.
        B_[0] = 1;
        
    #    计算线性复杂度
        N_ = 0;
        while ( N_ < M ):
            # 线性移位寄存器
            d = int(input_str[ii*M+N_])
            # d = S*CT 矩阵化的思路
            for i in xrange(1,L+1):
                d += C[i] * int(input_str[ii*M+N_-i])
            # print d
            d = d%2;

            if d == 1:
                for i in xrange(0,M):
                    T[i] = C[i]
                    P[i] = 0;
                
                for j in xrange(0,M):
                    # 这里有问题，需要好好的修改修改
                    if N_-m >= M:
                        # print "C",C
                        # print "B",B_
                        # print "P",P
                        break;
                    if B_[j] == 1:
                        # print j+N_-m,j,N_,m
                        P[j+N_-m] = 1
                for i in xrange(0,M):
                    C[i] = (C[i] + P[i])%2
                

                if  L <= N_/2 :
                    L = N_ + 1 - L
                    m = N_
                    for i in xrange(0,M):
                        B_[i] = T[i]

            N_ += 1

        parity = (M+1)%2
        if parity == 0: 
            sign = -1
        else:
            sign = 1
        mean = M/2.0 + (9.0+sign)/36.0 - 1.0/pow(2, M) * (M/3.0 + 2.0/9.0)

        parity = M%2
        if parity == 0:
            sign = 1
        else:
            sign = -1
        T_ = sign * (L - mean) + 2.0/9.0;
        
        if T_ <= -2.5:
            nu[0] += 1
        elif  T_ > -2.5 and T_ <= -1.5:
            nu[1] += 1
        elif T_ > -1.5 and T_ <= -0.5:
            nu[2] += 1
        elif T_ > -0.5 and T_ <= 0.5:
            nu[3] += 1
        elif T_ > 0.5 and T_ <= 1.5:
            nu[4] += 1
        elif T_ > 1.5 and T_ <= 2.5:
            nu[5] += 1
        else:
            nu[6]+=1

    chi2 = 0.00;
    # for i in xrange(0,K+1):

    # for ( i=0; i<K+1; i++ ) 
    #     fprintf(stats[TEST_LINEARCOMPLEXITY], "%4d ", (int)nu[i]);
    for i in xrange(0, K+1):
        chi2 += pow(nu[i]-N*pi[i], 2) / (N*pi[i]);

    p_value = igamc(K/2.0, chi2/2.0);

    return p_value

def linearComplexity_all(input_str,coordinates,queue=None,func_name=None):
    print "linearComplexity_all"
    result = []
    for coordinate in coordinates:
        p_value = linearComplexity(input_str[coordinate[0]:coordinate[1]+1],8)
        result.append(p_value)
    if queue!=None and func_name!=None:
        # queue.put((result,func_name))
        queue.append((result,func_name))      
    print "linearComplexity_all end"
    return (result,func_name)


def main():
    input_str = open("../TestData/data.e").read(100000)
    print linearComplexity(input_str,8)
if __name__ == '__main__':
    main()