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

def get_p_array(input_str,coordinates,queue=None,func_name=None):
    result = np.array([])
    coordinates = list(coordinates)
    len_of_subsegments = len(coordinates)
    test_str = ""
    for coordinate in coordinates:
        test_str = input_str[coordinate[0]:coordinate[1]+1]
        p,q = VLSequence.p_q_count(test_str)
        result = np.append(result,p)
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
    for coordinate in coordinates:
        test_str = input_str[coordinate[0]:coordinate[1]+1]
        p,q = VLSequence.p_q_count(test_str)
        result = np.append(result,q)
    # result = result/(len(test_str)/2)
    if queue!=None and func_name!=None:
        # queue.put((result,func_name))
        queue.append((result,func_name))    
    return (result,func_name)

def get_q_array_chi_square(q_array,m):
    """
        计算观察值和我们的标准值之间的差异
        q_array 是观察到的每一条序列中的q值
        m为分段大小
    """
    stat_hist = np.histogram(q_array,bins=range(0,int(math.floor(m/2))+2))
    print stat_hist,"111111"
    array_len = len(q_array)
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


 
        
    
    
