# coding:utf-8
"""
    这个配置文件主要是用于配置当前电脑的TestData的路径
"""

import platform
from nist_sts_python import runs,blockFrequency,frequency,matrix,DFT,VL,\
            NonOverlappingTemplateMatchings,overlappingTemplateMatchings,\
            universal,linearComplexity,serial,approximateEntropy,cusum,randomExcursions
import numpy as np
base_path_config = {
    "windows":"F:/TestData/",
    "linux":"/home/dm007/TestData/",
    "macos":"/Users/houseyoung/TestData/"
}

nist_func_set = [
    {"func":runs.runs,"args":(None),"func_name":"runs","cache":np.array([]),"uniform_rate":None},
    {"func":blockFrequency.block_frequency,"args":(None),"func_name":"BF","cache":np.array([]),"uniform_rate":None},
    {"func":frequency.frequency,"args":(None),"func_name":"F","cache":np.array([]),"uniform_rate":None},
    {"func":DFT.DiscreteFourierTransform,"args":(None),"func_name":"DFT","cache":np.array([]),"uniform_rate":None},
    {"func":NonOverlappingTemplateMatchings.NonOverlappingTemplateMatchings,"args":(None),"func_name":"NoTM","cache":np.array([]),"uniform_rate":None},
    {"func":overlappingTemplateMatchings.OverlappingTemplateMatchings,"args":(None),"func_name":"OTM","cache":np.array([]),"uniform_rate":None},
    # {"func":universal.universal,"args":(None),"func_name":"uni","cache":np.array([])},
    {"func":linearComplexity.linearComplexity,"args":(None),"func_name":"lc","cache":np.array([]),"uniform_rate":None},
    {"func":serial.serial,"args":(None),"func_name":"serial","cache":np.array([]),"uniform_rate":None},
    {"func":approximateEntropy.approximateEntropy,"args":(None),"func_name":"AE","cache":np.array([]),"uniform_rate":None},
    {"func":cusum.CumulativeSums,"args":(None),"func_name":"cusum","cache":np.array([]),"uniform_rate":None},
    {"func":randomExcursions.randomExcursions,"args":(None),"func_name":"re","cache":np.array([]),"uniform_rate":None},
    # {"func":VL.get_p_array,"args":(None),"func_name":"VL_P","cache":np.array([]),"uniform_rate":None},
    # {"func":VL.get_q_array,"args":(None),"func_name":"VL_q","cache":np.array([]),"uniform_rate":None},
]



def getTestDataPath():
    """
        根据当前操作系统的类型来判断
    """
    sysstr = platform.system()
    if sysstr == "Windows":
        return base_path_config.get("windows")
    elif sysstr == "Linux":
        return base_path_config.get("linux")
    elif sysstr == "Darwin":
        return base_path_config.get("macos")
    else:
        return None

def main():
    print getTestDataPath()

if __name__ == '__main__':
    main()