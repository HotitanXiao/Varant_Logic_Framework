# coding:utf-8
"""
作者: H.Y
日期: 
描述: 计算变质逻辑当中的内容的
"""
from MainFrame import VLSequence
import numpy as np

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
