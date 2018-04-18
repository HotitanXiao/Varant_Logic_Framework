# coding:utf-8
"""
    本工具包当中的各种函数方法的测试
"""
from local_settings import getTestDataPath
from MainFrame import VLSequence,Segmentor
from nist_sts_python import VL
import numpy as np
"""
    卡方估计
    针对q分布的卡方估计测试
"""
from nist_sts_python import VL

def vl_q_distribution_chi_square_test(input_str,m):
    """
    """
    coordinates = Segmentor.segmentor(input_str,m,m)
    q_array = []
    q_array,func_name = VL.get_q_array(input_str,coordinates)
    print q_array
    print VL.get_q_array_chi_square(q_array,m)

def vlCLibTest(inptu_str):
    """
    """
    import VLTest
    p,q = VLTest.PyVLTestForChar(inptu_str,8)
    p = np.array(p);
    q = np.array(q);


def main():
    test_path = getTestDataPath()
    file_name = test_path+"/2018-03/AES/aes_All_A_std.enc.char"
    input_str = open(file_name,"r").read(1000)
    vlCLibTest(input_str)
    # vl_q_distribution_chi_square_test(input_str,16)
    
    

if __name__ == '__main__':
    main()