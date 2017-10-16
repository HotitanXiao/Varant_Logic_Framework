# coding:utf-8
"""
作者: H.Y
日期: 
描述: 游程检测
"""
import math 
def runs(input_str,n):
    S = 0;
    for k in xrange(0,len(input_str)):
        if (input_str[k] == "1"):
            S += 1
    pi = float(S)/n
    if (math.fabs(pi - 0.5) > (2.0 / math.sqrt(n))):
        p_value = 0.0
    else:
        V = 1
        for k in xrange(1,n):
            if(input_str[k] != input_str[k-1] ):
                V += 1
        erfc_arg = math.fabs(V - 2.0 * n * pi * (1-pi)) / (2.0 * pi * (1-pi) * math.sqrt(2*n))
        p_value = math.erfc(erfc_arg)
    return p_value

def runs_all(input_str,coordinates,result_queue=None,func_name=None):
    result = []
    for coordinate in coordinates:
        test_str = input_str[coordinate[0]:coordinate[1]+1]
        p_value = runs(input_str[coordinate[0]:coordinate[1]+1],len(test_str))
        result.append(p_value)
    if result_queue and func_name:
        result_queue.put((result,func_name))
    return result

# def main():
#     a = "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"
#     print runs(a,100)

# if __name__ == '__main__':
#     main()
