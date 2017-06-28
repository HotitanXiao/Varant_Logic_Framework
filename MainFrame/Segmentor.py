# coding:utf-8
"""
作者: H.Y
日期: 
描述: 本文件里么都是分段操作的函数
"""

def segmentor(input_str, segment_size, offset):
    """
    参数:
        input_str,输入字符串
        segment_size,分段大小
        offset, 滑动距离
    输出: 各个分段点的起始、结束索引
    描述: 整体就是一个滑动窗口
    """
    len_of_str = len(input_str)
    start_index = 0
    end_index = start_index + segment_size - 1
    yield (start_index, end_index)
    while start_index < len_of_str and end_index+segment_size < len_of_str:
        start_index += offset
        end_index = start_index + segment_size - 1
        yield (start_index, end_index)