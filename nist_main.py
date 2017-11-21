# coding:utf-8
"""
作者: H.Y
日期: 
描述: 采用nist的方式来计算的结果
"""
from MainFrame import Segmentor,VLSequence,BitFilter
from MainFrame.sort import HeapSort
from Visualize import nist_plot
from nist_sts_python import runs,blockFrequency,frequency
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Process

def main():
    runs_p_value_array = []
    freq_p_value_array = []
    input_str = open("/home/dm007/TestData/ANU.char", "rb").read()
    # input_str = open('/home/dm007/TestData/TYUT_8bit_10.txt', "rb").read()
    segment_size = 1024
    coordinates = Segmentor.segmentor(input_str=input_str, segment_size=segment_size,offset=segment_size)
    # for coordinate in coordinates:
    #     runs_p_value = runs.runs(input_str[coordinate[0]:coordinate[1]+1],segment_size)
    #     freq_p_value = frequency.frequency(input_str[coordinate[0]:coordinate[1]+1])
    #     runs_p_value_array.append(runs_p_value)
    #     freq_p_value_array.append(freq_p_value)

    # matrix,xedges,yedges = np.histogram2d(runs_p_value_array,freq_p_value_array,bins=[100,100],range=[[0,1],[0,1]])

    # result = BitFilter.max_2d_filter(input_str,matrix,segment_size,segment_size)
    runs_p_value_array = []
    freq_p_value_array = []
    
    # 记录当前的p或q 数量的最大值
    p_count_array = []
    q_count_array = []
    pq_count_array = []
 
    # VLVisualize.vl_plot1d(p_array,q_array,m=segment_size,mod="p")
    p_count_max,q_count_max,pq_count_max = None,None,None
    p_temp,q_temp,pq_temp = None,None,None
    m_set = [1024]


    for m in m_set:
        # for i in xrange(0,m+1):
        #     shifted_str = VLSequence.string_right_shift(input_str,i)
        coordinates = Segmentor.segmentor(input_str=input_str, segment_size=m,offset=m)
        nist_plot.nist_multi_plot(input_str,coordinates)

if __name__ == '__main__':
    main()