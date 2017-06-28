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

def vl_plot1d(p_array,q_array,m,mod="",ylim=None,**kwargs):
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

    filename = utils.create_filename(mod=mod,m=m,**kwargs)
    p_max_index = y.argmax()
    p_count_max = y.max()

    right = 10*m/11
    top = p_count_max
    p_max_p = math.ceil(binEdges[p_max_index])
    # print y,binEdges
    bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
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
    plt.savefig("./Result/%s" % filename +".png")
    plt.close()
    return p_count_max



def vl_plot2d(p_array,q_array,m,title,mod=""):
    """
    参数:
    输出:
    描述: 二维的输出
    """

    if p_type == "2dp":
        x_lim = y_lim = (0,m+1)
        plt.xlabel("pi")
        plt.ylabel("pi+1")
        bins = [m,m]
        plot_range = [[0,m],[0,m]]
    elif p_type == "2dq":
        x_lim = y_lim = (0,m/2 + 1)
        plt.xlabel("qi")
        plt.ylabel("qi+1")
        bins = [m/2,m/2]
        plot_range = [[0,m/2],[0,m/2]]
    elif p_type == "2dpq":
        x_lim = (0,m +1)
        y_lim = (0,m/2 + 1)
        plt.xlabel("p")
        plt.ylabel("q")
        bins = [m,m/2 + 1]
        plot_range = [[0,m],[0,m/2]]
    

