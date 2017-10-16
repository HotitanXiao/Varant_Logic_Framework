# coding:utf-8
"""
作者: H.Y
日期: 
描述: 块內频数检测
"""
from mathUtils import *

def block_frequency(input_str,M,n):
    """
    参数: 
    输出: 
    描述: 
    """
    N = int(n/M)
    all_sum = .0
    for i in xrange(0,N):
        block_sum = .0
        for j in xrange(0,M):
            block_sum += int(input_str[j+i*M])
        pi = block_sum/M
        v = pi - 0.5
        all_sum += v*v
    chi_squared = 4.0 * M * all_sum
    p_value = igamc(N/2.0,chi_squared/2.0)
    return p_value

def block_frequency_all(input_str,coordinates,M=100):
    result = []
    for coordinate in coordinates:
        test_str = input_str[coordinate[0]:coordinate[1]+1]
        p_value = block_frequency(test_str,M,len(test_str))
        result.append(p_value)
    return result