# coding:utf-8
"""
作者: H.Y
日期: 
描述: 采用nist的方式来计算的结果
"""
from MainFrame import Segmentor,VLSequence,BitFilter
from MainFrame.sort import HeapSort
from Visualize import nist_plot,nist_plot_1d
from Visualize.utils import create_path
from nist_sts_python import runs,blockFrequency,frequency
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Process
import local_settings


import os,sys


def list_file(path):
    """
    """
    dir_list = os.listdir(path)
    result = []
    for line in dir_list:
        print line,os.path.splitext(path+line)[1],os.path.splitext(path+line)[1]
        if os.path.splitext(path+line)[1] and\
            os.path.splitext(path+line)[1] == ".char" :
            result.append(line)

    return result

def process():
    """ 
        批量处理文件
    """
    basepath = local_settings.getTestDataPath()+"/2018-03-13/"
    file_list = list_file(basepath)


# m_set = [1024,1500]
# length_set = [-1]
m_set = [1021,1022,1023,1024,1025,1026,1027]
length_set = [-1]
def go(basepath="",filename="",read_length=length_set[0]):
    runs_p_value_array = []
    freq_p_value_array = []
    # input_str = open("/home/dm007/TestData/ANU.char", "rb").read()
    # read_length =8000000
    input_str = open(basepath+filename, "rb").read(read_length)

    segment_size = 1024

    runs_p_value_array = []
    freq_p_value_array = []
    
    # 记录当前的p或q 数量的最大值
    p_count_array = []
    q_count_array = []
    pq_count_array = []
 
    # VLVisualize.vl_plot1d(p_array,q_array,m=segment_size,mod="p")
    p_count_max,q_count_max,pq_count_max = None,None,None
    p_temp,q_temp,pq_temp = None,None,None
    
    # 一个用于记录通过通过率的文件
    
    for m in m_set:
        # 创建保存测试文档得路径
        result_path = basepath+"/results/m=%s/" % m
        if not os.path.exists(result_path):
            os.mkdir(result_path)
        coordinates = Segmentor.segmentor(input_str=input_str, segment_size=m,offset=m)
        save_path = basepath + "results/"+ filename + "/len=%s/m=%s" %(read_length/10000,m)
        save_path = create_path(save_path)
        nist_plot.nist_multi_plot(input_str,coordinates,save_filename=filename,save_path=save_path,filename=filename.split(".")[0])
        # 这里输出nist 的通过率
        nist_prob_file = open(basepath + "results/"+ filename + "/len=%s/m=%s" %(read_length/10000,m)+"nist_prob.csv","w")
        for func in nist_plot.func_set:
            nist_prob_file.write("%s,%s,%s\n" %(func["func_name"],np.where(func["cache"] > 0.01)[0].size,np.where(func["cache"] > 0.01)[0].size/float(func["cache"].size)) )
        nist_prob_file.close()

            
        

if __name__ == '__main__':
    file_list = list_file(local_settings.getTestDataPath()+"/2018-03/Quantum/") 
    basepath = local_settings.getTestDataPath()+"/2018-03/Quantum/"
    for file_name in file_list: 
        print file_name
        for read_length in length_set:
            go(basepath,file_name,read_length)
