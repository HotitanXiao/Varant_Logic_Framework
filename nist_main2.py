# coding:utf-8
"""
作者: H.Y
日期: 
描述: 采用nist的方式来计算的结果
本文件用于处理一维的结果
每个文件生成单独的一维结果
操作步骤
列出文件
创建m=x的文件夹
创建每个文件的文件夹
开始绘制图像
绘制图像的时候并记录运行时间

"""
from MainFrame import Segmentor,VLSequence,BitFilter
from MainFrame.sort import HeapSort
from Visualize import nist_plot,nist_plot_1d
from nist_sts_python import runs,blockFrequency,frequency
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Process


import os,sys



class VLFile():
    def __init__(self,filename,size=None):
        self.filename = filename
        self.input_str = ""
        self.input_str = open(filename,"rb").read(size)
        self.segment_map = {}
        # self.current_lenth = size
        # self.input_str_list = {}

    def segmente(self,m):
        if m<1:
            raise Exception(u"分段不能小于等于0")
        else:
            coordinates = Segmentor.segmentor(input_str=self.input_str, segment_size=m,offset=m)
            print coordinates
            self.segment_map[m] = {"m":m,"coordinates":coordinates,"results":None}
    




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
    basepath = "D:/TestData/2018-01-23/"
    file_list = list_file(basepath)


m_set = [512,1024,2048]
readlenth_set = [800000,8000000,40000000,80000000]
vlfilelist = {}

def vlgo(basepath="",filename="",readlenth=None):
    # input_str = open("/home/dm007/TestData/ANU.char", "rb").read()
    if not vlfilelist.get(filename):
        vlfile = VLFile(basepath+filename,readlenth)
        vlfilelist[filename] = vlfile
    else:
        vlfile = vlfilelist.get(filename)
    for m_size in m_set:
        # for i in xrange(0,m+1):
        #     shifted_str = VLSequence.string_right_shift(input_str,i)
        # 创建保存测试文档得路径
        result_path = basepath+"results/len=%s/m=%s/%s" % (readlenth/10000,m_size,filename)
        if not os.path.exists(result_path):
            os.makedirs(result_path)
        vlfile.segmente(m=m_size)
        nist_plot_1d.nist_multi_plot_single(vlfile.input_str,vlfile.segment_map[m_size]["coordinates"],save_path=result_path)
        vlfile.segment_map[m_size]["results"] = nist_plot_1d.get_result()
        nist_plot_1d.clean_cache()


def plot_all_file_func_compare():
    """
        将所有的文件的统一函数处理结果放在同一个plot当中
    """
    pass



if __name__ == '__main__':
    """
        文件的参数处理及结果的处理顺序
        |文件读取大小
        |m大小
        |文件
        |结果
            |各种的函数方法

    """
    basepath = "D:/TestData/2018-01-23/"
    file_list = list_file(basepath)
    # 先确定读取的文件大小
    for readlenth in readlenth_set:
        # 开始读取文件
        for file in file_list:
            vlgo(basepath,file,readlenth)
    # nist_plot_1d.close_all()
    # 随便找一个结果集，然后从里面拿出使用了哪些函数
        for func_name in vlfilelist[vlfilelist.keys()[0]].segment_map[m_set[0]]["results"]:
            # import pdb;pdb.set_trace()
            for segment_type in m_set:
                for vlfile_name in vlfilelist:
                    vlfile = vlfilelist[vlfile_name]
                    vlfile.segment_map[segment_type]
                    """
                        results 里面存放了各种函数所产生的数据结果
                        {funcname,cache}
                    """
                    t = vlfile.segment_map[segment_type]["results"][func_name]["cache"]
                    vlfile.segment_map[segment_type]["results_hist"] = np.histogram(t,bins=np.arange(0,1.0,0.01))
                    # import pdb;pdb.set_trace()
                    plt.plot(vlfile.segment_map[segment_type]["results_hist"][1],np.append(vlfile.segment_map[segment_type]["results_hist"][0],0),label=vlfile_name)
                    
                leg = plt.legend(loc='best', ncol=2, mode="expand", shadow=True, fancybox=True)
                leg.get_frame().set_alpha(0.6)
                plt.savefig("%s/results/len=%s/m=%s/%s.png"%(basepath,readlenth/10000,segment_type,func_name),dpi=100)
                plt.close("all")
        vlfilelist = {}
    # plt.show()


    # 现在获取了所有的数据内容了，可以开始生成一些对比图


def tow_file_compare_plot(vlfile1,vlfile1):
    """
        进行两个文件的比较输出
    """
    pass

