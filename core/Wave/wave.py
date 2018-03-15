# -*-coding:utf-8 -*-
# File Name: wave_test.py
# Author   : H.Y
# Date     : 2015-11-6

import os
import random
import numpy as np
from ..Gorilla import Exhaust
from ..Gorilla import basic

ones = Exhaust.ones
one_zeros = Exhaust.one_zeros


class Wave(object):
    """此类用于产生具有周期性质的wave"""
    waves_set = {}             # 调试时候使用，用于存放生成的结果，并save

    def __init__(self, cycle=10, end_round=10000):
        super(Wave, self).__init__()
        self.cycle = cycle
        self.end_round = end_round

    def square_wave_to_mem(self, cycle=10, end_round=1000):
        i = 0
        result_str = ''
        while i < end_round:
            result_str += '1'*cycle
            result_str += '0'*cycle
            i += 1
        return result_str

    def complex_square_wave_to_mem(self, pattern="101110", end_round=1000):
        """
        用于产生周期稍微复杂一点的方波
        """
        i = 0
        result_str = ''
        print "pattern is %s" % pattern
        while i < end_round:
            result_str += pattern
            i += 1
        self.waves_set[pattern] = result_str
        return result_str

    def random_cycle_wave_to_mem(self, end_round=10000, random_range=(1, 30)):
        """
        产生一个随机周期的波普通方波,这个东西还是有问题的
        """
        i = 0
        result_str = ''
        while i < end_round:
            result_str += '1'*random.randint(random_range[0], random_range[1])
            result_str += '0'*random.randint(random_range[0], random_range[1])
            i += 1
        return result_str

    def save_result_str(self, temp_file_path):
        for key in self.waves_set.keys():
            outputfile = open("d:/TestData/%s" % key, 'wb')
            outputfile.write(self.waves_set[key])
        outputfile.close()

class Tools():
    """
    此类事用于对产生的01字符串进行相关的操作的
    """
    def get(self):
        pass
    def get_file_size(self, absolute_filename=''):
        """
        获取文件大小
        """
        return os.path.getsize(absolute_filename)

    def xor_str(self, string1='', string2='', compare_len=0):
        """
        将两个01字符串进行异或，并输出到文件当中。
        """
        result_str = ''
        if compare_len == 0:
            return result_str
        index = 0
        while index < compare_len:
            if string1[index] == string2[index]:
                result_str += '0'
            else:
                result_str += '1'
            index += 1
        return result_str

    def xor_file(self, filename1='', filename2='',
                 outputfile="d:\\result.dat"):
        try:
            file1_size = self.get_file_size(filename1)
            in_file1 = open(filename1)
            fiel2_size = self.get_file_size(filename2)
            in_file2 = open(filename2)
            buffer1 = in_file1.read(file1_size)
            buffer2 = in_file2.read(fiel2_size)
            outputfile = open(outputfile, 'wb')
            result = self.xor_str(
                buffer1,
                buffer2,
                min([file1_size, fiel2_size]))
            outputfile.write(result)
        except Exception, e:
            raise e


def multi_wave_xor(end_round=100, patterns=['1010110010', '1100101'],
                   cycles=[6, 10], random=False):
    """
    多波异或, 最后可以加入一个随机周期的0-1数组异或起来
    """
    print 'in %s' % cycles
    wave_set = []
    Wave_tools = Wave()
    if len(patterns) > 0:
        wave_craetor = Wave_tools.complex_square_wave_to_mem
        wave_parameters = patterns  # 用于产生最终波的参数
    elif len(cycles) > 0:
        print 'cycles'
        wave_craetor = Wave_tools.square_wave_to_mem
        wave_parameters = cycles

    tools = Tools()
    for parameter in wave_parameters:
        wave_set.append(wave_craetor(parameter, end_round))
    
    print "cycles is %s" % cycles
    # 准备开始异或的事情了
    result_wave = wave_set[0]  # 获取到第一条方波形数据
    for wave in wave_set[1:len(wave_parameters)]:
        result_wave = tools.xor_str(result_wave, wave,
                                    min(len(result_wave), len(wave)))
    if random:
        # 最后的一次异或将和一个随机变周期方波进行
        random_wave = Wave_tools.random_cycle_wave_to_mem(end_round)
        result_wave = tools.xor_str(result_wave,
                                    random_wave,
                                    min(len(result_wave), len(random_wave)))
    outputfile = open("d:/TestData/xorwave", 'wb')
    outputfile.write(result_wave)
    outputfile.close()
    Wave_tools.save_result_str("")
    return result_wave


def remove_temp_file(filename1='', filename2=''):
    """
    删除临时文件用的函数，如果模式不是文件模式的话，
    则此函数不会被调用
    """
    os.remove(filename1)
    os.remove(filename2)


def get_3d_data(end_round=1000, cycles=[12, 8, 2],
                window_size=10, random=False):
    xorwave = multi_wave_xor(end_round, cycles, random)
    result = basic.window_statstic(window_size,
                                   strbuffer=xorwave,
                                   offset=6)
    return basic.convert_pos(result)
