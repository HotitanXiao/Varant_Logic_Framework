# coding:utf-8
"""
Author:H.Y
FileName:Autocorrelateion
Date:2018-04-12
Descripthon:本文件是用于测量一个01序列的自相关特性的
"""
import numpy as np
import local_settings
from Visualize import utils
from matplotlib import pyplot as plt

def auto_correlateion(input_str,lags):
    """
    Author: H.Y
    Date: 2018-04-12
    Params: 
        input_str:输入01序列
    Descripthon: 返回01序列的自相关系数
    """
    n = len(input_str)
    t = map(lambda x: int(x),input_str)
    t = np.array(t)
    result = [np.correlate(t[i:]-t[i:].mean(),t[:n-i]-t[:n-i].mean())[0]\
        /(t[i:].std()*t[:n-i].std()*(n-i)) \
		for i in range(1,lags+1)]
    return result


def main():
    test_data_path = local_settings.getTestDataPath()
    target_path =  test_data_path+"/2018-03/AES/"
    # input_str = open(test_data_path+"/2018-03/Quantum/8bit-split/8bit.char.split0").read(1000000)
    # input_str = open(test_data_path+"/2018-03/Quantum/8bit.char").read(1000000)
    files = utils.list_file(target_path)
    for filename in files:
        input_str = open(target_path+filename).read(1000000)
        offset_range = 1000
        correlateion_result = auto_correlateion(input_str,offset_range)
        plt.plot(range(1,offset_range+1),correlateion_result)
        plt.ylim(-0.2,0.2)
        plt.savefig("filename=%s,offset=%s"%(filename,offset_range))

    # input_str = open(test_data_path+"/2018-03/RC4/8bit-split/"+"vrc4_nist_8bit.txt.split6").read()
    # input_str = open(test_data_path+"/2018-03/Quantum/8bit-split/"+"8bit.char.split7").read()



if __name__ == '__main__':
    main()