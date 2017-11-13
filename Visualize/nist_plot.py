# coding:utf-8
"""
作者: H.Y
日期: 
描述: 用于测试nist的可视化工具
"""
from nist_sts_python import runs,blockFrequency,frequency,matrix,DFT,VL,\
            NonOverlappingTemplateMatchings,overlappingTemplateMatchings,\
            universal,linearComplexity,serial,approximateEntropy,cusum
from matplotlib.colors import LogNorm
import numpy as np
import matplotlib.pyplot as plt
import copy
from multiprocessing import Process,Queue

func_set = [
    {"func":runs.runs_all,"args":(None),"func_name":"runs","cache":np.array([])},
    {"func":blockFrequency.block_frequency_all,"args":(None),"func_name":"BF","cache":np.array([])},
    {"func":frequency.frequency_all,"args":(None),"func_name":"F","cache":np.array([])},
    {"func":DFT.DiscreteFourierTransform_all,"args":(None),"func_name":"DFT","cache":np.array([])},
    {"func":NonOverlappingTemplateMatchings.NonOverlappingTemplateMatchings_all,"args":(None),"func_name":"NoTM","cache":np.array([])},
    {"func":overlappingTemplateMatchings.OverlappingTemplateMatchings_all,"args":(None),"func_name":"OTM","cache":np.array([])},
    {"func":universal.universal_all,"args":(None),"func_name":"uni","cache":np.array([])},
    {"func":linearComplexity.linearComplexity_all,"args":(None),"func_name":"lc","cache":np.array([])},
    {"func":serial.serial_all,"args":(None),"func_name":"serial","cache":np.array([])},
    {"func":approximateEntropy.approximateEntropy_all,"args":(None),"func_name":"AE","cache":np.array([])},
    {"func":cusum.CumulativeSums_all,"args":(None),"func_name":"cusum","cache":np.array([])},
    {"func":VL.get_p_array,"args":(None),"func_name":"VL_P","cache":np.array([])},# -*- coding: utf-8 -*-
# Filename: gorilla.py
from __future__ import division
import math
import matplotlib.pyplot as plt
import enum
import numpy as np
import  time


class GorilaBasis(object):
    """该类包含了基础的数学操作，获得的
    结果是杨辉三角形的某一个数字的拆分结果"""    

    def __init__(self):
        self.name='GorilaBasis'        
    def chose(self,N,n): #组合数-N选n
        """传说中的组合数学"""
        return math.factorial(N)//math.factorial(n)//math.factorial(N-n)
    
    def redundants(self,n,k,c): #一个函数,就是网上的那个
        """函数名:redundants
            参数：n 杨辉三角第n行 n>=1
                      k 第n行的第k列
                      c circular culaster
            说明:计算某个(n,k)单元"""
        if ((n-k)<k):
            return self.redundants(n,n-k,c)
        else:
            return (self.chose(abs(n-k),abs(c))*n*self.chose(abs(k-1),abs(c-1))//(n-k))
        
    
    def midProccess(self,inputArray,timeFactor=1,opcode="1111"):
        """
        函数名: midProccess
        参数: inputArray 四元np数组
                timeFactor
                opcode
        返回值: 一个nparray，是计算结果
        说明:
        """
        result = self.powerOperation(inputArray[1:5],timeFactor)
        result = result*self.operation(opcode)
        inputArray[1:5] = result
      #  print inputArray
        return inputArray
        


    def powerOperation(self,inputArray,timeFactor):
        """函数名：powerOperation
            参数：inputArray 输入的多元向量
                        timeFcator 表示次方数
            返回值：一个nparray，是计算结果
            说明：输入一个多元向量，其每个
                    元素进行次方运算    
        """
        #print inputArray
        nparry =  np.array(inputArray)
        nparry = nparry**timeFactor
        #print nparry
        return nparry


    def operation(self,opcode):
        """
        函数名：operation
        参数:
        返回值:
        说明:
        """
        #用于存放转换结果的数组
        opcodeArray = [0,0,0,0]
        if len(opcode) != 4:
            #报错
            print "error-opcode 不合法"
        else:
            for x in xrange(0,4):
                if opcode[x] == '0':
                    pass
                elif opcode[x] == '1':
                    opcodeArray[x] = 1
                elif opcode[x] == '2':
                    opcodeArray[x] = -1

        return np.array(opcodeArray)


                
        
        
    def  cRange(self,n,k): #似乎是计算某个区间的
        if ((n-k)<k):
            return self.cRange(n,n-k) #这里和C语言不一样，递归处也要return
        elif k==0:
            return [0]
        else:            
            return range(1,k+1)
    
    def createBasis(self,N,timeFactor=1,opcode="1111"):
        result = []
        for k in xrange(0,N+1):
            for c in self.cRange(N,k):
                #y=c
                y= N-k-c
                #z=c
                z = k-c
                a = self.redundants(N,k,c)
                result.append(self.midProccess(np.array([a,y,c,c,z]),timeFactor,opcode))
        return result    
    #得到一个三角形
    def getTriangle_SingleRow(self,N):
        """得到一行的所有拆分单元"""
        yanghuiTriangle = []
        for k in xrange(0,N+1):
            row = []
            #print'k'+str(k)
            for c in self.cRange(N,k):
                #print 'c'+str(c)
                row.append(self.redundants(N,k,c))
                #print row
            yanghuiTriangle.append(row)
        return yanghuiTriangle
    
    #使用列表推倒式的版本
    # def createBasis2(self,N):
    #     return np.array([[redundants(N,k,c),N-k-c,c,c,k-c] for k in xrange(0,N+1) for c in cRange(N,k)])

    def getMask(self,type):
        """根据输入类型生成对应的掩码"""
        pass


## End of gorrila.py
def test1(N=10):
    test = GorilaBasis()
    for x in xrange(N,N+1):
        print test.getTriangle_SingleRow(x)
if __name__ == '__main__':
    # from timeit import Timer
    # t1=Timer("test1()","from __main__ import test1")
    # print t1.timeit(100)
    test1()
    #print t1.timeit(100000)
    # test = GorilaBasis()
    # for x in xrange(0,10):
    #     print test.cRange(9,x)

    {"func":VL.get_q_array,"args":(None),"func_name":"VL_q","cache":np.array([])},
]


def process_cache_multi_processing(input_str,coordinates,queue):
    """
    参数: 
    输出: 
    描述: 进行并发运算，快速处理各个处理方法的值
    进行特征计算的主函数
    主要用于进行进程阻塞的
    """
    print "house-process"*10
    p_p = []
    for i in xrange(0,len(func_set)):
        p_process = Process(target=func_set[i]["func"],args=(input_str,coordinates,queue,i,))
        p_process.daemon = True
        p_p.append(p_process)
    for p in p_p:
        p.start()

def process_cache(input_str,coordinates,queue):
    for i in xrange(0,len(func_set)):
        print "now--processing%s" % func_set[i]["func_name"]
        func_set[i]["func"](input_str,coordinates,queue,i)
        


def nist_multi_plot(input_str,coordinates,row=len(func_set),col=len(func_set),**kwargs):
    # q = Queue()
    # 一进来就直接进行处理
    # p = Process(target=process_cache,args=(input_str,coordinates,q,))
    # p.start()
    # p.join()
    q = []

    bins = [100,100]
    plot_range = [[0,1],[0,1]]
    temp_coordinates = list(coordinates)

    process_cache(input_str,temp_coordinates,q)
    # print len(q)
    for i in xrange(0,len(q)):
        result = q[i]
        func_set[result[1]]["cache"] = np.array(result[0])

    log_file = open("log.txt","wb")
    fig = plt.gcf()
    fig.set_size_inches(18.5*5, 10.5*5)
    
    for y in xrange(1,row+1):
        for x in xrange(1, col+1):
            a = plt.subplot(row,col+1,(y-1)*(col+1)+x)
            # a = plt.subplot(row,col+1,(y-1)*(col+1)+x)
            # 先判断是否有缓存机制
            if func_set[y-1]["cache"].any():
                p_array = func_set[y-1]["cache"]
                print "has_cache %s" % func_set[y-1]["func_name"]
            else:
                print "has_no_cache %s" % func_set[y-1]["func_name"]
                p_array = func_set[y-1]["func"](input_str,temp_coordinates)
                func_set[y-1]["cache"] = np.array(p_array)
            if x == y:
                q_array = p_array
            else:
                q_array = func_set[x-1]["func"](input_str,temp_coordinates)
                if func_set[x-1]["cache"].any():
                    q_array = func_set[x-1]["cache"]
                    print "has_cache %s" % func_set[x-1]["func_name"]
                else:
                    print "has_no_cache %s" % func_set[y-1]["func_name"]
                    q_array = func_set[x-1]["func"](input_str,temp_coordinates)
                    func_set[x-1]["cache"] = np.array(q_array)
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
