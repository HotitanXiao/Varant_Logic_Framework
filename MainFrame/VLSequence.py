# coding:utf-8
"""
作者: H.Y
日期: 2017-06-22
描述: 用于获取字符串特征值的模块
"""

def p_q_count(input_str):
    """
    参数: input_str-0-1比特的字符串
    输出: （p,q）
    描述: 计算改序列的p、q的值
    """
    p_count = 0
    q_count = 0
    i = 0
    str_len = len(input_str)
    while i < str_len:
        if input_str[i] == '0' and input_str[(i+1)%str_len] == '1':
            q_count += 1
            # 避免在环尾重复计数1
            if i+1 < str_len:
                p_count += 1
            i += 2
        else:
            if input_str[i] == '1':
                p_count += 1
            i += 1
    return (p_count, q_count)

def four_tuple(input_str, offset):
    """
    参数: input_str-0-1比特的字符串,offset 配对距离
    输出: 四元特征组
    描述: 获取四元组特征
    """
    pass