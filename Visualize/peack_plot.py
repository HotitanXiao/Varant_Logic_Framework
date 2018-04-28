# coding:utf-8
"""
    输出的是进行移位分析以后，q分析的峰值变化图示
"""
import numpy as np
from matplotlib import pyplot as plt
from nist_sts_python import VL

def peak_plot(stat_array,m,offset,mod="p"):
    """
        stat_array是一个统计结果的集合，其数据结构是一个二位数组
        [x*m]*N, m x N维的一个二维数组
        m是关注的template、变值分布的一个基本区间
        mod 是当前是p还是q，主要是用在拟合优度部分

        说明：
            该函数的用途是输出一个图示结果，该结果是所有统计结果最大值（峰值），所在的位置
            最大值的位置，还有拟合优度的变化
    """
    peaks_pos = [0]*(len(stat_array))
    peak_values = [0]*(len(stat_array))
    chi_square = [0]*len(stat_array)
    for row_index in xrange(0,len(stat_array)):
        # print stat_array[row_index]
        a = np.max(stat_array[row_index])
        t = np.where(stat_array[row_index]==a)
        peaks_pos[row_index] = t[0][0]
        peak_values[row_index] = stat_array[row_index][t[0][0]]
        if mod == "p":
            chi_square[row_index] = VL.get_p_array_chi_square(p_stat_array=stat_array[row_index],m=m)
        else:
            chi_square[row_index] = VL.get_q_array_chi_square(q_stat_array=stat_array[row_index],m=m)
    plt.subplot(311)
    plt.plot(range(0,len(stat_array)),peaks_pos)
    plt.subplot(312)
    plt.plot(range(0,len(stat_array)),peak_values)
    plt.subplot(313)
    plt.plot(range(0,len(stat_array)),chi_square)
    return plt;


def main():
    test_data = np.array([
        [1,2,3,4,5],
        [5,4,3,2,1],
        [4,5,3,2,1]
    ])
    # peak_plot(test_data,4)

if __name__ == '__main__':
    main()