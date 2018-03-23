# coding:utf-8
"""
作者: H.Y
日期: 
描述: 
主要是针对1dp，2dp，1dq，2dq，2dpq的检测图
"""

from MainFrame import Segmentor,VLSequence,BitFilter
from MainFrame.sort import HeapSort
from Visualize import VLVisualize
import numpy as np
import matplotlib.pyplot as plt
import local_settings 
from Visualize import utils


def plot_lines_in_one_ax():
    """
    """
    pass


def plot(base_file_path,target_filename,read_length):
    """
    参数: 
    输出: 
    描述: 
    """
    p_array = []
    q_array = []
    # base_file_path = local_settings.getTestDataPath()
    input_str = open(base_file_path+target_filename, "rb").read(read_length)
    segment_size = 128
    coordinates = Segmentor.segmentor(input_str=input_str, segment_size=segment_size,offset=segment_size)
    for coordinate in coordinates:
        p, q = VLSequence.p_q_count(input_str[coordinate[0]:coordinate[1]+1])
        p_array.append(p)
        q_array.append(q)
    matrix,xedges,yedges = np.histogram2d(p_array,q_array,bins=[segment_size,segment_size/2],range=[[0,segment_size],[0,segment_size/2]])

    # result = BitFilter.max_2d_filter(input_str,matrix,segment_size,segment_size)
    p_array = []
    q_array = []

    # 记录当前的p或q 数量的最大值
    p_count_array = []
    q_count_array = []
    twodp_count_array = []
    twodq_count_array = []
    pq_count_array = [] 
 
    # VLVisualize.vl_plot1d(p_array,q_array,m=segment_size,mod="p")
    p_count_max,q_count_max,twodq_count_max,twodp_count_max,pq_count_max = None,None,None,None,None
    p_temp,q_temp,twodp_temp,twodq_temp,pq_temp = None,None,None,None,None
    m_set = [128]
    for m in m_set:
        for i in xrange(0,m+1):
            # shifted_str = VLSequence.string_right_shift(result[1],i)
            shifted_str = input_str
            # 上面的东西是用来判断移位操作的
            coordinates = Segmentor.segmentor(input_str=shifted_str, segment_size=m,offset=m)
            for coordinate in coordinates:
                p, q = VLSequence.p_q_count(shifted_str[coordinate[0]:coordinate[1]+1])
                p_array.append(p)
                q_array.append(q)

            p_temp = VLVisualize.vl_plot1d(p_array=p_array,q_array=q_array,m=m,mod="p",source=target_filename,ylim=1,rs=i)
            q_temp = VLVisualize.vl_plot1d(p_array=p_array,q_array=q_array,m=m,mod="q",source=target_filename,ylim=1,rs=i)

            twodq_temp = VLVisualize.vl_plot2d(p_array=p_array,q_array=q_array,m=m,mod="2dq",source=target_filename,rs=i)
            twodp_temp = VLVisualize.vl_plot2d(p_array=p_array,q_array=q_array,m=m,mod="2dp",source=target_filename,rs=i)
            pq_temp = VLVisualize.vl_plot2d(p_array=p_array,q_array=q_array,m=m,mod="2dpq",source=target_filename,rs=i)
            if i == 0:
                p_count_max = p_temp
            p_count_array.append(p_temp)
            q_count_array.append(q_temp)
            twodp_count_array.append(twodp_temp)
            twodq_count_array.append(twodq_temp)
            pq_count_array.append(pq_temp)


            # VLVisualize.vl_plot1d(p_array,q_array,m=segment_size,mod="q",rs=i)
            p_array = []
            q_array = []

        # 归一化一下
        p_count_array = np.array(p_count_array)
        p_count_array = p_count_array/float(np.max(p_count_array))
        q_count_array = np.array(q_count_array)
        q_count_array = q_count_array/float(np.max(q_count_array))
        twodp_count_array = np.array(twodp_count_array)
        twodp_count_array = twodp_count_array/float(np.max(twodp_count_array))
        twodq_count_array = np.array(twodq_count_array)
        twodq_count_array = twodq_count_array/float(np.max(twodq_count_array))
        pq_count_array = np.array(pq_count_array)
        pq_count_array = pq_count_array/float(np.max(pq_count_array))
        
        VLVisualize.plot1d(range(0,m+1),p_count_array,{"mod":"p_count","rs":i,"source":target_filename,"m":m})
        VLVisualize.plot1d(range(0,m+1),q_count_array,{"mod":"q_count","rs":i,"source":target_filename,"m":m})
        VLVisualize.plot1d(range(0,m+1),twodp_count_array,{"mod":"2dp_count","rs":i,"source":target_filename,"m":m})
        VLVisualize.plot1d(range(0,m+1),twodq_count_array,{"mod":"2dq_count","rs":i,"source":target_filename,"m":m})
        VLVisualize.plot1d(range(0,m+1),pq_count_array,{"mod":"pq_count","rs":i,"source":target_filename,"m":m})

        # 最后将所有的图像画到同一张图片上
        fig, ax = plt.subplots()
        dashes = [10, 5, 100, 5]
        # 输出三条线的
 
        line1, = ax.plot(range(0,m+1), p_count_array, '--', linewidth=1, label='p_count')
        line2, = ax.plot(range(0,m+1), q_count_array, '--', linewidth=1, label='q_count')
        # line3, = ax.plot(range(0,m+1), twodp_count_array, '--', linewidth=1, label='2dp_count')
        # line4, = ax.plot(range(0,m+1), twodq_count_array, '--', linewidth=1, label='2dq_count')
        line5, = ax.plot(range(0,m+1), pq_count_array, '--', linewidth=1, label='2dpq_count')
        ax.legend(loc='upper center')
        plt.plot()
        plt.savefig("./_m=%s-_3lines=.png" % m)
        # 输出五条线的
        line3, = ax.plot(range(0,m+1), twodp_count_array, '--', linewidth=1, label='2dp_count')
        line4, = ax.plot(range(0,m+1), twodq_count_array, '--', linewidth=1, label='2dq_count')
        ax.legend(loc='upper center')
        plt.plot()
        plt.savefig("./_m=%s_all=.png" % m)
        plt.close()
        p_count_array = []
        q_count_array = []
        pq_count_array = []
        twodp_count_array = []
        twodq_count_array = []
    # output_file = open("./TestData/filter_xor.char","wb")

def main():
    """
        主函数
    """
    base_path = local_settings.getTestDataPath()
    target_path = base_path+"2018-03/"
    files = utils.list_file(target_path)
    plot(target_path,files[0],80000000)


if __name__ == '__main__':
    main()