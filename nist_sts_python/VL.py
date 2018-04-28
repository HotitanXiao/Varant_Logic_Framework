# coding:utf-8
"""
作者: H.Y
日期: 
描述: 计算变质逻辑当中的内容的
"""
from MainFrame import VLSequence
import numpy as np
from core.Gorilla.gorilla import GorilaBasis
import math
from multiprocessing import Pool
import VLTest

def get_p_array(input_str,coordinates,queue=None,func_name=None):
    result = np.array([])
    coordinates = list(coordinates)
    len_of_subsegments = len(coordinates)
    test_str = ""

    m = coordinates[0][1]+1 - coordinates[0][0]
    p,q = VLTest.PyVLTestForChar(input_str=input_str,m=m)
    # for coordinate in coordinates:
    #     test_str = input_str[coordinate[0]:coordinate[1]+1]
    #     p,q = VLSequence.p_q_count(test_str)
    #     result = np.append(result,p)
    # print "House--------------------------------get_p_array"
    result = np.array(p)
    # result = result/len(test_str)
    if queue!=None and func_name!=None:
        # queue.put((result,func_name))   
        queue.append((result,func_name))    
    return (result,func_name)
    

def get_q_array(input_str,coordinates,queue=None,func_name=None):
    result = np.array([])
    coordinates = list(coordinates)
    len_of_subsegments = len(coordinates)
    test_str = ""
    m = coordinates[0][1]+1 - coordinates[0][0]
    p_,q_ = VLTest.PyVLTestForChar(input_str=input_str,m=m)
    # for coordinate in coordinates:
    #     test_str = input_str[coordinate[0]:coordinate[1]+1]
    #     p,q = VLSequence.p_q_count(test_str)
    #     result = np.append(result,q)
    # result = result/(len(test_str)/2)
    # print "House--------------------------------get_q_array"
    # print q_
    result = np.array(q_)
    # print "House--------------------------------get_q_array"
    if queue!=None and func_name!=None:
        # queue.put((result,func_name))
        queue.append((result,func_name))   
    # print get_q_array_chi_square(result,m)
    return (result,func_name)

def get_p_array_chi_square(p_array=None,p_stat_array=None,m=8):
    """
    Author: H.Y
    Date: 2018-04-18
    Params: 
    Descripthon: 该方法是算p的拟合优度的，p就是二项式系数，所以里面用组合函数来计算就可以了
    """
    if not p_stat_array.any():
        stat_hist = np.histogram(p_array,bins=range(0,int(math.floor(m/2))+2))
        array_len = len(p_array)
    else:
        stat_hist = (p_stat_array,range(0,m/2+2))
        array_len = sum(p_stat_array)
    print "array_len=",array_len

    base_distribution = GorilaBasis()
    chi_rate = 0
    observed_stat_array = []
    for q in xrange(0,m+1):
        alpha = base_distribution.getKview(m,q) #理论值 在2^N下产生的
        if alpha == 0:
            print "******---***"*10
            print "in get_p_array_chi_square zeros occur N=%s,q=%s" % (m,q)
        else:
            observed_stat = stat_hist[0][q]/float(array_len)
            observed_stat_array.append(observed_stat)
            print "p = %s,observed_count=%s observed_stat=%s,base_distibute=%s" % (q,stat_hist[0][q],observed_stat,alpha)
            chi_rate += ( observed_stat - alpha )**2 / alpha
    print sum(observed_stat_array),observed_stat_array
    return chi_rate    

def get_q_array_chi_square(q_array=None,q_stat_array=None,m=8):
    """
        计算观察值和我们的标准值之间的差异
        q_array 是观察到的每一条序列中的q值
        m为分段大小
    """
    if not q_stat_array.any():
        stat_hist = np.histogram(q_array,bins=range(0,int(math.floor(m/2))+2))
        array_len = len(q_array)
    else:
        stat_hist = (q_stat_array,range(0,m/2+2))
        array_len = sum(q_stat_array)

    
    print "array_len=",array_len
    base_distribution = GorilaBasis()
    chi_rate = 0
    observed_stat_array = []
    for q in xrange(0,int(math.floor(m/2)+2)):
        alpha = base_distribution.getCview(m,q) #理论值 在2^N下产生的
        if alpha == 0:
            print "******---***"*10
            print "in get_q_array_chi_square zeros occur N=%s,q=%s" % (m,q)
        else:
            observed_stat = stat_hist[0][q]/float(array_len)
            observed_stat_array.append(observed_stat)
            print "q = %s,observed_count=%s observed_stat=%s,base_distibute=%s" % (q,stat_hist[0][q],observed_stat,alpha)
            chi_rate += ( observed_stat - alpha )**2 / alpha
    print sum(observed_stat_array),observed_stat_array
    return chi_rate


 
        
    
    
