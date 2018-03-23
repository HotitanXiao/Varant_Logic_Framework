# coding:utf-8
"""
    这个文件是在获取到了所有比较精细的统计结果的基础上
    然后进行一个合并统计的操作
    例如我当前获得的统计数据长度喂7
    [0,1,2,3,4,5,6]
    我可以对这些数据进行相应的合并操作比如说是0，1合并，2，3合并
    或者是0，2合并，1，3合并
"""
from Visualize import nist_plot_for_nist_main3 as npnm3

from MainFrame import Segmentor,VLSequence,BitFilter
from MainFrame.sort import HeapSort
from nist_sts_python import runs,blockFrequency,frequency
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Process


import os,sys


import local_settings


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
    basepath = "D:/TestData/2018-03-13/"
    file_list = list_file(basepath)


m_set = [2048,512,32]
# readlenth_set = [800000,8000000,40000000]
readlenth_set = [5000000]
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
        npnm3.nist_multi_plot_single(vlfile.input_str,vlfile.segment_map[m_size]["coordinates"],save_path=result_path)
        vlfile.segment_map[m_size]["results"] = npnm3.get_result()
        npnm3.clean_cache()


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
    basepath = local_settings.getTestDataPath() + "2018-03-13/"
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
                    # vlfile.segment_map[segment_type]["results_hist"] = np.histogram(t,bins=np.arange(0,1.0,0.01))
                    vlfile.segment_map[segment_type]["results_hist"] = np.histogram(t,np.arange(min(t),max(t)+1,1))
                    # import pdb;pdb.set_trace()
                    # plt.plot(vlfile.segment_map[segment_type]["results_hist"][1],np.append(vlfile.segment_map[segment_type]["results_hist"][0],0),".",label=vlfile_name)
                    plt.plot(vlfile.segment_map[segment_type]["results"][func_name]["merge_cache"][0],vlfile.segment_map[segment_type]["results"][func_name]["merge_cache"][1],".",label=vlfile_name)
                    print vlfile_name,func_name,segment_type,vlfile.segment_map[segment_type]["results_hist"][0][0],len(t)
                    
                leg = plt.legend(loc='best', ncol=2, mode="expand", shadow=True, fancybox=True)
                leg.get_frame().set_alpha(0.6)
                plt.savefig("%s/results/len=%s/m=%s/%s.png"%(basepath,readlenth/10000,segment_type,func_name),dpi=100)
                plt.close("all")
        vlfilelist = {}
    # plt.show()


    # 现在获取了所有的数据内容了，可以开始生成一些对比图


def tow_file_compare_plot(vlfile1,vlfile2):
    """
        进行两个文件的比较输出
    """
    pass

