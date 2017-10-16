# coding:utf-8
"""
作者: H.Y
日期: 2017-06-27
描述: 可视化部分的函数
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import utils
import os
from MainFrame.sort import HeapSort

SAVE_PATH = "./Result/"

def check_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return True


        

def plot1d(x_array,y_array,filename_args,**kwargs):
    """
    """
    related_dir,filename = utils.create_filename(**filename_args)
    check_dir(SAVE_PATH+related_dir)
    plt.bar(x_array,y_array,**kwargs)
    plt.plot()
    plt.savefig(SAVE_PATH+related_dir+filename +".png")
    plt.close()




def vl_plot1d(p_array,q_array,m,mod="",source="",ylim=None,**kwargs):
    """
    参数:
    输出:
    描述:一维的输出
        kwargs 中包含的其他一些参数奖体现在文件名当中，此中的参数并不参与计算
    """
    if mod == "p":
        bins = m
        r_array = p_array
        y,binEdges = np.histogram(r_array, bins=bins,range=[0,m])
    elif mod == "q":
        bins = m/2
        r_array = q_array
        y,binEdges = np.histogram(r_array, bins=bins,range=[0,m/2])
    related_dir,filename = utils.create_filename(source=source,mod=mod,m=m,**kwargs)
    check_dir(SAVE_PATH+related_dir)
    p_max_index = y.argmax()
    p_count_max = y.max()

    right = 10*m/11
    top = p_count_max
    p_max_p = math.ceil(binEdges[p_max_index])
    # print y,binEdges
    bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
    # 归一化
    y = np.divide(y,float(len(r_array)))
    title ="m=%s p_count_max=%s(p=%s)"%(m,y[p_max_index],p_max_p)
    top_text = "m:%s\n%s_count_max:%s\np:%s\nbins:%s" %(m,mod,y[p_max_index],p_max_p,len(binEdges)-1)
    plt.text(right,top, top_text,
        horizontalalignment='right',
        verticalalignment='top',)
    # plt.text(100, y[p_max_index], 'm=1 \np_count_max=10', style='italic',bbox={'alpha':0, 'pad':10})
    plt.title(title)
    plt.xlim(0,bins)
    if ylim:
        plt.ylim(0,ylim)
    plt.xlabel(mod)
    plt.ylabel("count") 
    plt.bar(bincenters,y,align='center')
    plt.plot()
    plt.savefig(SAVE_PATH+related_dir+filename+".png")
    plt.close()
    return p_count_max



def plot2d(p_array,q_array,m,mod="",**kwargs):
    """
    参数: 
    输出: 
    描述: 
    """
    bins = [100,100]
    plot_range = [[0,1],[0,1]]
    # matrix,xedges,yedges = np.histogram2d(array_1,array_2,bins=bins,range=plot_range)
    matrix,xedges,yedges = np.histogram2d(p_array,q_array,bins=bins,range=plot_range)
    plt.hist2d(p_array,q_array,bins=bins,range=plot_range,normed=True)
    kwargs["m"] = m
    kwargs["mod"] = mod
    related_dir,filename = utils.create_filename(**kwargs)
    check_dir(SAVE_PATH+related_dir)
    plt.savefig(SAVE_PATH+related_dir+filename+".png")
    plt.close()


def vl_plot2d(p_array,q_array,m,mod="",**kwargs):
    """
    参数:
    输出:
    描述: 二维的输出
    """
    array_1 = None
    array_2 = None
    if mod == "2dp":
        x_lim = y_lim = (0,m+1)
        plt.xlabel("pi")
        plt.ylabel("pi+1")
        bins = [m,m]
        plot_range = [[0,m],[0,m]]
        array_1 = p_array
        array_2 = utils.array_right_shift(p_array,1)
        # matrix,xedges,yedges = np.histogram2d(array_1,array_2,bins=bins,range=plot_range)

    elif mod == "2dq":
        x_lim = y_lim = (0,m/2 + 1)
        plt.xlabel("qi")
        plt.ylabel("qi+1")
        bins = [m/2,m/2]
        plot_range = [[0,m/2],[0,m/2]]
        array_1 = q_array
        array_2 = utils.array_right_shift(q_array,1)
        # matrix,xedges,yedges = np.histogram2d(array_1,array_2,bins=bins,range=plot_range)
    elif mod == "2dpq":
        x_lim = (0,m +1)
        y_lim = (0,m/2 + 1)
        plt.xlabel("p")
        plt.ylabel("q")
        bins = [m,m/2 + 1]
        plot_range = [[0,m],[0,m/2]]
        array_1 = p_array
        array_2 = q_array
    matrix,xedges,yedges = np.histogram2d(array_1,array_2,bins=bins,range=plot_range)
    
    plt.hist2d(array_1,array_2,bins=bins,range=plot_range,normed=True)
    kwargs["m"] = m
    kwargs["mod"] = mod
    related_dir,filename = utils.create_filename(**kwargs)
    check_dir(SAVE_PATH+related_dir)
    
    plt.savefig(SAVE_PATH+related_dir+filename+".png")
    plt.close()

    # 找出其中的最大值并返回
    max_count = HeapSort.VLHeapSort(matrix).top(1)
    return max_count[0]["value"] 



    

