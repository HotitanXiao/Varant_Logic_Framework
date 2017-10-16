# coding:utf-8
"""
作者: H.Y
日期: 
描述: 计算变质逻辑当中的内容的
"""
from MainFrame import VLSequence
import numpy as np

def get_p_array(input_str,coordinates,input_queue=None,func_name=None):
    result = np.array([])
    for coordinate in coordinates:
        test_str = input_str[coordinate[0]:coordinate[1]+1]
        p,q = VLSequence.p_q_count(test_str)
        result = np.append(result,p)
    
    result = result/len(test_str)
    if input_queue and func_name:
        input_queue.put((result,func_name))
    return result
    

def get_q_array(input_str,coordinates,input_queue=None,func_name=None):
    result = np.array([])
    for coordinate in coordinates:
        test_str = input_str[coordinate[0]:coordinate[1]+1]
        p,q = VLSequence.p_q_count(test_str)
        result = np.append(result,q)
    result = result/(len(test_str)/2)
    if input_queue and func_name:
        input_queue.put((result,func_name))
    return result
