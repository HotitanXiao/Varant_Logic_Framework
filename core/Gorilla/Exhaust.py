 # -*- coding: utf-8 -*-
# File Name: Exhuast.py
# Author   : H.Y
# Date     : 2015-4-1


def exhuast(N=1):
    """设计是两层字典数据结构"""
    maxNumber = 2**N
    result = {}
    binstr_ones = 0
    binstr_one_zeros = 0
    for x in xrange(0, maxNumber):
        binstr = bin(x)[2:].zfill(N)  # 在前方填充使字符串长度到N
        binstr_ones = ones(binstr, N)
        binstr_one_zeros = one_zeros(binstr, N)
        # 开始判断操作
        if binstr_ones in result:
            b = result[binstr_ones]
            if binstr_one_zeros in b:
                #  如果有1-0的序列的话就进行自增
                b[binstr_one_zeros] += 1
            else:
                b[binstr_one_zeros] = 1
        else:
            result[binstr_ones] = {binstr_one_zeros: 1}

    return result


def ones(binstr, N):
    """根据输入的二进制串计算1的个数"""
    count = 0
    if N == 1:
        return count
    for x in xrange(0, N):
        if binstr[x] == '1':
            count = count+1
    return count


def one_zeros(binstr, N):
    """计算01的个数，需要考虑循环的操作,N表示0-1向量的位长
    """
    count = 0
    if N == 1:
        return count
    for x in xrange(0, N):
        if (binstr[x] == '0' and binstr[(x+1) % N] == '1'):
            count = count + 1
    return count


def p_and_q(binstr, N):
    """
    同时统计p和q的算法
    """
    p_count = 0                # 表示1的个数
    q_count = 0                # 表示01块的个数
    if N == 1:
        return (p_count, q_count)
    for x in xrange(0, N):
        if binstr[x] == '1':    # 发现一个1
            p_count += 1
            if binstr[(N - 1 + x) % N] == '0':
                q_count += 1

    return (p_count, q_count)

def exhuast_str(N=1):
    """设计是两层字典数据结构"""
    maxNumber = 2**N
    result = {}
    binstr_ones = 0
    binstr_one_zeros = 0
    for x in xrange(0, maxNumber):
        binstr = bin(x)[2:].zfill(N)  # 在前方填充使字符串长度到N
        binstr_ones = ones(binstr, N)
        binstr_one_zeros = one_zeros(binstr, N)
        # 开始判断操作
        if binstr_ones in result:
            b = result[binstr_ones]
            if binstr_one_zeros in b:
                #  如果有1-0的序列的话就进行自增
                b[binstr_one_zeros] = b[binstr_one_zeros] +";"+binstr
            else:
                b[binstr_one_zeros] = binstr
        else:
            result[binstr_ones] = {binstr_one_zeros: binstr}

    return result

def test1(N=8):
    b = exhuast(N)
    
   # print b
if __name__ == '__main__':
    from timeit import Timer
    for x in xrange(2,32):
        t1=Timer("test1("+str(x)+")","from __main__ import test1")
        print  t1.timeit(1)
