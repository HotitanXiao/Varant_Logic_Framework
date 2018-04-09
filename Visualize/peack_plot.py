# coding:utf-8
"""
    输出的是进行移位分析以后，q分析的峰值变化图示
"""
import numpy as np
from matplotlib import pyplot as plt

def peak_plot(stat_array,m):
    """
        stat_array是一个统计结果的集合，其数据结构是一个二位数组
        [x*m]*N, m x N维的一个二维数组
        m是关注的template、变值分布的一个基本区间


        说明：
            该函数的用途是输出一个图示结果，该结果是所有统计结果最大值（峰值），所在的位置
            最大值的位置，还有拟合优度的变化
    """
    peaks_pos = [0]*(m+1)
    peak_values = [0]*(m+1)
    for row_index in xrange(0,len(stat_array)):
        # print stat_array[row_index]
        a = np.max(stat_array[row_index])
        t = np.where(stat_array[row_index]==a)
        peaks_pos[row_index] = t[0][0]
        peak_values[row_index] = stat_array[row_index][t[0][0]]
    print peak_values
    plt.subplot(211)
    plt.plot(range(0,m+1),peaks_pos)
    plt.subplot(212)
    plt.plot(range(0,m+1),peak_values)
    plt.show()

    print peaks

def main():
    test_data = np.array([
        [1,2,3,4,5],
        [5,4,3,2,1],
        [4,5,3,2,1]
    ])
    peak_plot(test_data,4)

if __name__ == '__main__':
    main()