# -*-coding:utf-8 -*-
# File Name: wave_projection.py
# Author   : H.Y
# Date     : 2015-11-10

import numpy as np
import matplotlib.pyplot as plt
import wave
from ..Gorilla import basic


def _getFileName(round, cycles, patterns, random, window_size, offset, projecttype):
    return "pt=" + projecttype +\
        "_r=" + str(round) +\
        "_p=" + str(patterns) +\
        "_c=" + str(cycles) + \
        "_rdm=" + bin(random)[2:] + \
        "_ws="+str(window_size) + \
        "_offset=" + str(offset)


def projection(end_round=1000, cycles=[12, 8, 2], random=False,
               window_size=10, offset=6, projecttype='p',
               patterns=['1010110010', '1100101']):
    """
    用于生成映射的数据，可选按p和按q映射
    """
    xorwave = wave.multi_wave_xor(end_round=end_round,
      patterns=patterns,
      cycles=cycles,
      random=random)
    print "window_size is %s" % window_size
    return basic.window_statstic_pjct(window_size, xorwave,
                                     offset, projecttype)


def process(end_round=1000, patterns=['10100', '110010'],
            cycles=[12, 7, 2], random=False,
            window_size=10, offset=6, projecttype='p',
            output_dir='./ouput'):
    data = projection(end_round=end_round,
                      cycles=cycles,
                      random=random,
                      window_size=window_size,
                      offset=offset,
                      projecttype=projecttype,
                      patterns=patterns)
    filename = output_dir + _getFileName(end_round, cycles, patterns, random,
                                         window_size, offset, projecttype)
    plt.xlabel(projecttype)
    plt.ylabel('count')
    print data
    plt.hist(data, facecolor='green')
    plt.savefig(filename)  # 保存文件了~走起
    plt.close('all')
