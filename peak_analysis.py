# coding:utf-8
"""
    观察一个序列的稳定性的，主要是通过滑动窗口进行
"""
import numpy as np
from Visualize import peack_plot
from MainFrame import VLSequence,Segmentor
import local_settings

def peak_analyze(input_str,m):
    """
        对这个东西进行循环移位，然后用滑动窗口判断他的稳定性
        输出两个数组
        peak_pos
        peak_value
        可以绘图
    """
    results_array = []
    for offset in xrange(0,m+1):
        print "shift offset = ",offset
        new_str = VLSequence.string_right_shift(input_str,offset)
        coordinates = Segmentor.segmentor(new_str,m,m)
        p_array = []
        q_array = []

        for coordinate in coordinates:
            p_count,q_count =  VLSequence.p_q_count(new_str[coordinate[0]:coordinate[1]+1])
            # print p_count,q_count
            q_array.append(q_count)
            p_array.append(p_count)
        # 统计完成
        print "offset = %s complete count now start stastic"
        q_stat_results,q_bins = np.histogram(q_array,bins=range(0,m/2+2))
        p_stat_results,p_bins = np.histogram(p_array,bins=range(0,m+2))
        results_array.append([p_stat_results,q_stat_results])
        print "offset = %s complete stats"
        
    # 完成了所有的统计了
    temp_array = np.array(results_array)
    q_stat_all = temp_array[:,0]
    # import pdb;pdb.set_trace()
    # print q_stat_all
    peack_plot.peak_plot(q_stat_all,m)

    



def main():
    base_path = local_settings.getTestDataPath()
    input_str = open(base_path+"/2018-03/RC4/vrc4_p[4,4,4,4]_q[1,2,3,4].char","rb").read(1000)
    peak_analyze(input_str,32)

if __name__ == '__main__':
    main()