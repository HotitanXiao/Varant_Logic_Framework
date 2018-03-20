# coding:utf-8
"""
作者: H.Y
日期: 
描述: 主要是一些辅助性的函数
    例如是：文件名的生成
"""
import os

def create_filename(source,m,mod,**kwargs):
    """
    参数: 
    输出: 
    描述: 文件名创建函数
            包括文件名和相对路径
    """
    file_name = ""
    related_dir = "%s/%s/%s/"%(source,mod,m)
    keys = kwargs.keys()
    keys.sort(reverse=True)
    for key in keys:
        file_name += "_%s=%s" %(key,kwargs[key])
    return (related_dir,file_name)

def array_right_shift(string,offset):
    offset = offset % len(string)
    return string[-offset:]+string[:-offset]

def list_file(path):
    """
        获取路径下已.char结尾的文件
    """
    dir_list = os.listdir(path)
    result = []
    for line in dir_list:
        print line,os.path.splitext(path+line)[1],os.path.splitext(path+line)[1]
        if os.path.splitext(path+line)[1] and\
            os.path.splitext(path+line)[1] == ".char" :
            result.append(line)

    return result