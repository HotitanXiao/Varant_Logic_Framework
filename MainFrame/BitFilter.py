# coding:utf-8
"""
作者: H.Y
日期: 2017-06-24
描述: 用于从分段中获取符合预期特征的
"""
from sort import HeapSort
import Segmentor
import VLSequence


class FeatureFilterUnit(object):
    """pass"""
    # TODO:mod 是控制匹配的维度的，暂时未实现该功能
    def __init__(self, feature_set, mod="1"):
        self.feature_set = feature_set
        self.mod = mod

    def equqal(self, p, q):
        for feature in self.feature_set:
            # print p,q,feature["y"],feature["x"]
            if p == feature["y"] and q == feature["x"]:
                return True
        return False
        

def max_p():
    """
    参数: 
    输出: 
    描述: 获取p最大序列
    """
    pass

def max_q():
    """
    参数: 
    输出: 
    描述: 获取q最大的序列
    """

    pass

def max_2d_filter(input_str,result_matrix,segment_size,offset,param1="p",param2="q"):
    """
    参数: 
    输出: 返回整个序列的下一个特征序列的位置
    描述: 两个特征值，
    """
    # TODO:在矩阵当中找到各种的最大值
    sortor = HeapSort.VLHeapSort(result_matrix)
    top = sortor.top(1)
    vl_filter = FeatureFilterUnit(top)
    print top
    coordinates = Segmentor.segmentor(input_str=input_str, segment_size=segment_size, offset=offset)
    result = []
    result_str = ""
    for coordinate in coordinates:
        p, q = VLSequence.p_q_count(input_str[coordinate[0]:coordinate[1]+1])
        if vl_filter.equqal(p, q):
            result.append(coordinate)
            result_str += input_str[coordinate[0]:coordinate[1]+1]
    return (result,result_str)