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

    # VLVisualize.vl_plot1d(p_array,q_array,m=segment_size,mod="p")
    p_count_max = None
    for i in xrange(0,128):
        shifted_str = VLSequence.string_right_shift(result[1],i)
        coordinates = Segmentor.segmentor(input_str=shifted_str, segment_size=segment_size,offset=segment_size)
        for coordinate in coordinates:
            p, q = VLSequence.p_q_count(shifted_str[coordinate[0]:coordinate[1]+1])
            p_array.append(p)
            q_array.append(q)
        temp = VLVisualize.vl_plot1d(p_array,q_array,m=segment_size,mod="p",ylim=p_count_max,rs=i)
        if i == 0:
            p_count_max = temp
        # VLVisualize.vl_plot1d(p_array,q_array,m=segment_size,mod="q",rs=i)
        p_array = []
        q_array = []
    # output_file = open("./TestData/filter_xor.char","wb")

if __name__ == '__main__':
    main()