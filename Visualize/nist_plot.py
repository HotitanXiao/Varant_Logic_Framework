# coding:utf-8
"""
作者: H.Y
日期: 
描述: 用于测试nist的可视化工具
"""
from nist_sts_python import runs,blockFrequency,frequency,matrix,DFT,VL,NonOverlappingTemplateMatchings
from matplotlib.colors import LogNorm
import numpy as np
import matplotlib.pyplot as plt
import copy
from multiprocessing import Process,Queue

func_set = [
    {"func":runs.runs_all,"args":(None),"func_name":"runs"},
    {"func":blockFrequency.block_frequency_all,"args":(None),"func_name":"BF","cache":np.array([])},
    {"func":frequency.frequency_all,"args":(None),"func_name":"F","cache":np.array([])},
    {"func":DFT.DiscreteFourierTransform_all,"args":(None),"func_name":"DFT","cache":np.array([])},
    {"func":NonOverlappingTemplateMatchings.NonOverlappingTemplateMatchings_all,"args":(None),"func_name":"NoTM","cache":np.array([])},
    {"func":OverlappingTemplateMatchings.OverlappingTemplateMatchings_all,"args":(None),"func_name":"OTM","cache":np.array([])},
    {"func":universal.universal_all,"args":(None),"func_name":"uni","cache":np.array([])},
    {"func":VL.get_p_array,"args":(None),"func_name":"VL_P","cache":np.array([])},
    {"func":VL.get_q_array,"args":(None),"func_name":"VL_q","cache":np.array([])},
]





def process_cache(input_str,coordinates,queue):
    """
    参数: 
    输出: 
    描述: 进行并发运算，快速处理各个处理方法的值
    进行特征计算的主函数
    主要用于进行进程阻塞的
    """
    p_p = []
    for i in xrange(0,len(func_set)):
        p_process = Process(target=func_set[i]["func"],args=(input_str,coordinates,queue,i,))
        p_process.daemon = True
        p_p.append(p_process)
    for p in p_p:
        p.start()


def nist_multi_plot(input_str,coordinates,row,col,**kwargs):
    q = Queue()
    # 一进来就直接进行处理
    p = Process(target=process_cache,args=(input_str,coordinates,q,))
    p.start()
    p.join()

    for i in xrange(0,q.qsize()):
        result = q.get()
        func_set[result[1]]["cache"] = result[0]

    bins = [100,100]
    plot_range = [[0,1],[0,1]]
    temp_coordinates = list(coordinates)
    log_file = open("log.txt","wb")
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    
    for y in xrange(1,row+1):
        for x in xrange(1, col+1):
            a = plt.subplot(row,col+1,(y-1)*(col+1)+x)
            a = plt.subplot(6,6,(y-1)*(col)+x)
            # 先判断是否有缓存机制
            if func_set[y-1]["func"]["cache"].any():
                p_array = func_set[y-1]["func"]["cache"]
            else:
                p_array = func_set[y-1]["func"](input_str,temp_coordinates)
                func_set[y-1]["func"]["cache"] = np.array(p_array)
            if x == y:
                q_array = p_array
            else:
                q_array = func_set[x-1]["func"](input_str,temp_coordinates)
                if func_set[y-1]["func"]["cache"].any():
                    q_array = func_set[y-1]["func"]["cache"]
                else:
                    q_array = func_set[y-1]["func"](input_str,temp_coordinates)
                    func_set[y-1]["func"]["cache"] = np.array(q_array)
            print func_set[y-1]["func_name"],len(p_array),func_set[x-1]["func_name"],len(q_array)
            matrix,xedges,yedges = np.histogram2d(p_array,q_array,bins=bins,range=plot_range)
            plt.hist2d(p_array,q_array,bins=bins,range=plot_range,norm=LogNorm())
            #plt.hist2d(p_array,q_array,bins=bins,range=plot_range)
            # plt.colorbar()
            a.set_title(func_set[y-1]["func_name"]+"_"+func_set[x-1]["func_name"])
        # 绘画单独的hist图样
        a = plt.subplot(row,col+1,(y-1)*(col+1)+col+1)
        p_array = func_set[y-1]["func"](input_str,temp_coordinates)
        plt.hist(p_array,bins=100)
        a.set_title(func_set[y-1]["func_name"])

    log_file.close()
    plt.tight_layout()
    plt.savefig("test.png")
    fig.savefig('test2png.png', dpi=100)

# def nist_list_plot(input_str,coordinates,**kwargs):
#     """
#     参数: 
#     输出: 
#     描述: 列出所有的hist图样
#     """
