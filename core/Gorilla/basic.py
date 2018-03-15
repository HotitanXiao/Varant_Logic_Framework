# -*-coding:utf-8 -*-
import Exhaust as ex
import numpy as np
ones = ex.ones
one_zeros = ex.one_zeros


def quantum_statstic_pjct(window_size=10, strbuffer='',
                         offset=1, projection='p'):
    """
    这个函数是用于生成一个映射的数据流，就不进行统计，只是标记
    这次统计得到的p，或q并加入到result数组中
    """
    ones_result = 0
    zeros_result = 0
    buffer_size = len(strbuffer)
    if buffer_size < 2:
        return
    result = np.array([])  # 存放统计结果的
    index = 0
    if projection == 'p':
        pjctfunc = ones
    else:
        one_flag = False
        pjctfunc = one_zeros
    while index < buffer_size-window_size:
        # 开始判断操作
        # pkey 是用于进行映射用的索引标记
        pkey = pjctfunc(strbuffer[index:index+window_size], window_size)
        ones_result += pkey
        zeros_result += (window_size - pkey)
        result = np.append(result, pkey)
        index = index+offset
    return (ones_result,zeros_result,result)



def window_statstic_pjct(window_size=10, strbuffer='',
                         offset=1, projection='p'):
    """
    这个函数是用于生成一个映射的数据流，就不进行统计，只是标记
    这次统计得到的p，或q并加入到result数组中
    """
    buffer_size = len(strbuffer)
    if buffer_size < 2:
        return
    result = np.array([])  # 存放统计结果的
    index = 0
    if projection == 'p':
        pjctfunc = ones
    else:
        pjctfunc = one_zeros
    while index < buffer_size-window_size:
        # 开始判断操作
        # pkey 是用于进行映射用的索引标记
        pkey = pjctfunc(strbuffer[index:index+window_size], window_size)
        result = np.append(result, pkey)
        index = index+offset
    return result


def window_statstic(window_size=10, strbuffer='', offset=1):
    """
    滑动窗口统计
    offset:表示每次窗口滑动的距离
    """
    buffer_size = len(strbuffer)
    if buffer_size < 2:
        return
    result = {}  # 存放统计结果的
    index = 0
    while index < buffer_size-window_size:
        # 开始判断操作
        # 取一个窗口
        binstr_ones = ones(strbuffer[index:index+window_size], window_size)
        binstr_one_zeros = one_zeros(
            strbuffer[index:index+window_size],
            window_size)
        if binstr_ones in result:
            p = result[binstr_ones]
            if binstr_one_zeros in p:
                # 如果有1-0的序列的话就进行自增
                p[binstr_one_zeros] += 1
            else:
                p[binstr_one_zeros] = 1
        else:
            result[binstr_ones] = {binstr_one_zeros: 1}
        index = index+offset
    return result


def convert_pos(result):
    """
    传入一个结果map，将结果map转换为
    """
    ppos = []  # 1的个数
    qpos = []  # 0-1的个数
    conpos = []  # 聚类个体数

    for cluster_index in result:
        for t in result[cluster_index]:
            ppos.append(cluster_index)
            qpos.append(t)
            conpos.append(result[cluster_index][t])
    return (ppos, qpos, conpos)
