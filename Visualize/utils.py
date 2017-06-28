# coding:utf-8
"""
作者: H.Y
日期: 
描述: 主要是一些辅助性的函数
    例如是：文件名的生成
"""


def create_filename(**kwargs):
    """
    参数: 
    输出: 
    描述: 文件名创建函数
    """
    file_name = ""
    keys = kwargs.keys()
    keys.sort(reverse=True)
    for key in keys:
        file_name += "_%s=%s" %(key,kwargs[key])
    return file_name