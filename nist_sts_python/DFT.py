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
    m = [0]*(len(S)/2+1)
    m[0] = math.sqrt(S[0].real*S[0].real)
    S = np.append(S,[0])
    # 这里估计也是计算错的 应该是这里的计算值有错误
    # print S[0]
    # print type(S[0])
    for i in xrange(1,len(S)/2):
		#m[i+1] = math.sqrt(math.pow(S[2*i+1],2)+math.pow(S[2*i+2],2))
        m[i] = math.sqrt(math.pow(S[i].real,2)+math.pow(S[i].imag,2))
    count = 0
    upperBound = math.sqrt(2.995732274*n);
    # 这里计算的有点不对
    for i in xrange(0,len(S)/2):
        if ( m[i] < upperBound ):
            count += 1;
    # count -= 1
    percentile = float(count)/(n/2)*100;
    N_l = float(count);
    N_o = float(0.95)*n/2.0;
    d = (N_l - N_o)/math.sqrt(n/4.0*0.95*0.05);
    p_value = math.erfc(math.fabs(d)/math.sqrt(2.0));
    return p_value

def DiscreteFourierTransform_all(input_str,coordinates,input_queue=None,func_name=None):
    result = []
    for coordinate in coordinates:
        p_value = DiscreteFourierTransform(input_str[coordinate[0]:coordinate[1]+1])
        result.append(p_value)
    if input_queue and func_name:
        input_queue.put((result,func_name))
    return result


def main():
    # a = "101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010"
    # a = "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"
    a = "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"
    print DiscreteFourierTransform(a)

if __name__ == '__main__':
    main()