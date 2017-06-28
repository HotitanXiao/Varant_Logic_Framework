# coding:utf-8
"""
作者: H.Y
日期: 2017-6-19
描述: 变值逻辑核心计算体系
    是将分段操作和过滤器相结合的
"""




def get_p_q_nonoverlap(filename,bit_length,m):
    """
    参数: 0-1比特的字符串
    输出: （p,q）
    描述: 计算改序列的p、q的值
    """
    p_array = []
    q_array = []
    file = open(filename,"rb")
    def read_and_cac(read_count):
        input_string = file.read(m*10000)
        coordinates = subsector.subsector_type1(input_string,m,False)
        for coordinate in coordinates:
            p, q = vlogic_analyze.process_nonoverlap(input_string[coordinate[0]:coordinate[1]+1])
            p_array.append(p)
            q_array.append(q)
    # read round
    read_round = bit_length / (m*10000)
    for x in xrange(0,read_round):
        read_and_cac(m*10000)
    left_length = bit_length%10000
    read_and_cac(left_length)
    # print len(p_q_array)
    return p_array,q_array


