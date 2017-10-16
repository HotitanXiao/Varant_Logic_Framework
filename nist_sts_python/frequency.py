# coding:utf-8
"""
作者: H.Y
日期: 
描述: 频数检测
"""
import math
from decimal import Decimal
def frequency(input_str):
    """
    参数: 
    输出: 
    描述: 计算每个字符串的p——value
    """
    sqrt2 = Decimal('1.41421356237309504880')
    all_sum = 0.0;
    for i in xrange(0,len(input_str)):
        all_sum += 2*int(input_str[i]) -1
    s_obs = math.fabs(all_sum)/math.sqrt(len(input_str))
    f = Decimal(str(s_obs))/sqrt2
    p_value = math.erfc(f)
    return p_value


def frequency_all(input_str,coordinates,input_queue=None,func_name=None):
    """
    参数: 
    输出: 
    描述: func_name可以是index，也是func的name
    """
    result = []
    for coordinate in coordinates:
        p_value = frequency(input_str[coordinate[0]:coordinate[1]+1])
        result.append(p_value)
    if input_queue and func_name:
        input_queue.put((result,func_name))
    return result
        