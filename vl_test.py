# coding:utf-8
"""
    这个图是专门用来生成变值图示
"""
from MainFrame import Segmentor,VLSequence,BitFilter
from MainFrame.sort import HeapSort
from nist_sts_python import VL
from Visualize import nist_plot,nist_plot_1d
from nist_sts_python import runs,blockFrequency,frequency
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Process


import os,sys


def main():
    input_str = open("D:/TestData/9bit.txt","rb").read()
    input_str_coordinates = Segmentor.segmentor(input_str,9,9)
    t = list(input_str_coordinates)
    p,func_name = VL.get_p_array(input_str,t)
    q,func_name = VL.get_q_array(input_str,t)
    print max(p)+1
    plt.hist2d(p,q,bins=(range(0,int(max(p)+2)),range(0,int(max(q))+2)))
    # plt.hist(p,bins=range(0,int(max(p))+2) )
    plt.show()

if __name__ == '__main__':
    main()