# coding:utf-8
"""
作者: H.Y
日期: 
描述: 离散傅立叶检测
"""
import math
import numpy as np

def DiscreteFourierTransform(input_str):
    """
    参数: 
    输出: 
    描述: 
    """
    n = len(input_str)
    input_array = map(lambda x:2*int(x)-1,input_str)
    input_array = np.array(input_array)
    S = np.fft.fft(input_array)
    m = abs(S)[:n/2]
    count = 0
    upperBound = math.sqrt(2.995732274*n);
    for i in xrange(0,len(S)/2):
        if ( m[i] < upperBound):
            count += 1;
    # count -= 1
    percentile = float(count)/(n/2)*100;
    N_l = float(count);
    N_o = float(0.95)*n/2.0;
    # print N_l,N_o
   
    d = (N_l - N_o)/math.sqrt((n*0.95*0.05)/4.0);
    p_value = math.erfc(math.fabs(d)/math.sqrt(2.0));
    return p_value

def DiscreteFourierTransform_all(input_str,coordinates,queue=None,func_name=None):
    print "DiscreteFourierTransform_all"
    result = []
    for coordinate in coordinates:
        p_value = DiscreteFourierTransform(input_str[coordinate[0]:coordinate[1]+1])
        result.append(p_value)
    if queue!=None and func_name!=None:
        # queue.put((result,func_name))
        queue.append((result,func_name))
    print "DiscreteFourierTransform_all end"
    return (result,func_name)


def main():
    # a = "101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010"
    # a = "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"
    # a = "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"
    a = "1001010011"
    print DiscreteFourierTransform(a)

    # a = [0.00000,1.61803,1.38197,-0.61803,3.61803,-2.00000,3.61803,-0.61803,1.38197,1.61803]

    # b = [0.00000,1.17557,4.25325,1.90211,2.62866,0.00000,2.62866,1.90211,4.25325,1.17557]
    # print dft_test(a)
    # print math.sqrt(2.995732274*10)
    # for(x,y) in zip(a,b):
    #     print math.sqrt(math.pow(x,2)+math.pow(y,2))

if __name__ == '__main__':
    main()