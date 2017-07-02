# coding:utf-8
"""
作者: H.Y
日期: 
描述: 
"""

from MainFrame import Segmentor,VLSequence,BitFilter
from MainFrame.sort import HeapSort
from Visualize import VLVisualize
import numpy as np
import matplotlib.pyplot as plt

def main():
    """
    参数: 
    输出: 
    描述: 
    """
    p_array = []
    q_array = []
    input_str = open("./TestData/test.bin.enc.char", "rb").read(1000000)
    segment_size = 128
    coordinates = Segmentor.segmentor(input_str=input_str, segment_size=segment_size,offset=segment_size)
    for coordinate in coordinates:
        p, q = VLSequence.p_q_count(input_str[coordinate[0]:coordinate[1]+1])
        p_array.append(p)
        q_array.append(q)
    matrix,xedges,yedges = np.histogram2d(p_array,q_array,bins=[segment_size,segment_size/2],range=[[0,segment_size],[0,segment_size/2]])

    result = BitFilter.max_2d_filter(input_str,matrix,segment_size,segment_size)
    p_array = []
    q_array = []
    
    # 记录当前的p或q 数量的最大值
    p_count_array = []
    q_count_array = []
    pq_count_array = []
 
    # VLVisualize.vl_plot1d(p_array,q_array,m=segment_size,mod="p")
    p_count_max,q_count_max,pq_count_max = None,None,None
    p_temp,q_temp,pq_temp = None,None,None
    m_set = [128]
    for m in m_set:
        for i in xrange(0,m+1):
            shifted_str = VLSequence.string_right_shift(result[1],i)
            coordinates = Segmentor.segmentor(input_str=shifted_str, segment_size=m,offset=m)
            for coordinate in coordinates:
                p, q = VLSequence.p_q_count(shifted_str[coordinate[0]:coordinate[1]+1])
                p_array.append(p)
                q_array.append(q)
            p_temp = VLVisualize.vl_plot1d(p_array=p_array,q_array=q_array,m=m,mod="p",source="AES-256-CBC",ylim=1,rs=i)
            q_temp = VLVisualize.vl_plot1d(p_array=p_array,q_array=q_array,m=m,mod="q",source="AES-256-CBC",ylim=1,rs=i)
            pq_temp = VLVisualize.vl_plot2d(p_array=p_array,q_array=q_array,m=m,mod="2dq",source="AES-256-CBC",rs=i)
            if i == 0:
                p_count_max = p_temp
            p_count_array.append(p_temp)
            q_count_array.append(q_temp)
            pq_count_array.append(pq_temp)

            # VLVisualize.vl_plot1d(p_array,q_array,m=segment_size,mod="q",rs=i)
            p_array = []
            q_array = []
        VLVisualize.plot1d(range(0,m+1),p_count_array,{"mod":"p_count","rs":i,"source":"AES-256-CBC","m":m})
        VLVisualize.plot1d(range(0,m+1),q_count_array,{"mod":"q_count","rs":i,"source":"AES-256-CBC","m":m})
        VLVisualize.plot1d(range(0,m+1),pq_count_array,{"mod":"pq_count","rs":i,"source":"AES-256-CBC","m":m})
        p_count_array = []
        q_count_array = []
        pq_count_array = []
    # output_file = open("./TestData/filter_xor.char","wb")

if __name__ == '__main__':
    main()