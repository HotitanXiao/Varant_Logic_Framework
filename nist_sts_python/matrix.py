# coding:utf-8
"""
作者: H.Y
日期: 
描述: 二元举证秩的计算
"""
import math
import numpy as np
MATRIX_FORWARD_ELIMINATION = 0
MATRIX_BACKWARD_ELIMINATION = 1

def compute_rank(M,Q,matrix):
    m=min([M,Q]);
    rank = 0
	# /* FORWARD APPLICATION OF ELEMENTARY ROW OPERATIONS */ 
    for i in xrange(0,m-1):
        if ( matrix[i][i] == 1 ):
            perform_elementary_row_operations(MATRIX_FORWARD_ELIMINATION, i, M, Q, matrix);
        else:
            # /* matrix[i][i] = 0 */
            if ( find_unit_element_and_swap(MATRIX_FORWARD_ELIMINATION, i, M, Q, matrix) == 1 ):
				perform_elementary_row_operations(MATRIX_FORWARD_ELIMINATION, i, M, Q, matrix)

	# /* BACKWARD APPLICATION OF ELEMENTARY ROW OPERATIONS */ 
    for i in xrange(m-1,0,-1):
        if ( matrix[i][i] == 1 ):
            perform_elementary_row_operations(MATRIX_BACKWARD_ELIMINATION, i, M, Q, matrix);
        else:
            # /* matrix[i][i] = 0 */
            if ( find_unit_element_and_swap(MATRIX_BACKWARD_ELIMINATION, i, M, Q, matrix) == 1 ):
				perform_elementary_row_operations(MATRIX_BACKWARD_ELIMINATION, i, M, Q, matrix);
	rank = determine_rank(matrix);
	return rank;

def determine_rank(input_matrix):
    i, j, rank, allZeroes=0,0,0,0
    rank = len(input_matrix);
    for i in xrange(0,len(input_matrix)):
        allZeroes = 1
        for j in xrange(0,len(input_matrix[0])):
			if ( input_matrix[i][j] == 1 ):
				allZeroes = 0;
				break;
        if ( allZeroes == 1 ):
			rank -= 1;
    return rank;

def perform_elementary_row_operations(flag, i, M, Q, A):
    """
    参数: A是输入的比特矩阵
    输出: 
    描述: 
    """
    j = k = 0
	
    if ( flag == MATRIX_FORWARD_ELIMINATION ):
        for j in xrange(i+1,M):
            if ( A[j][i] == 1 ):
                for k in xrange(i,Q):
                    A[j][k] = (A[j][k] + A[i][k]) % 2
	
    else:
        for j in xrange(i-1,-1,-1):
            if ( A[j][i] == 1 ):
                for k in xrange(0,Q):
					A[j][k] = (A[j][k] + A[i][k]) % 2;

def find_unit_element_and_swap(flag,i,M,Q,A):

    index,row_op=0,0;
	
    if ( flag == MATRIX_FORWARD_ELIMINATION ):
        index = i+1
        while ( (index < M) and (A[index][i] == 0) ):
			index += 1
			if ( index < M ):
				row_op = swap_rows(i, index, Q, A)
    else:
        index = i-1;
        while ( (index >= 0) and (A[index][i] == 0) ):
            index -= 1
            if ( index >= 0 ):
				row_op = swap_rows(i, index, Q, A)
	return row_op;


def swap_rows(i,index,Q,A):
    temp = None;
    for p in xrange(0,Q):
		temp = A[i][p]
		A[i][p] = A[index][p]
		A[index][p] = temp

def m_rank(input_str):
    n = len(input_str)
    N = n/(32*32)
    p_value = product = chi_squared = arg1 = 0.0
    p_32 = p_31 = p_30 = R = F_32 = F_31 = F_30 = 0.0
    
    if(not N):
        print "Error: Insuffucient # Of Bits To Define An 32x32"
        return 0.0
    else:
        r = 32
        product = 1
        for i in xrange(0,r):
            product *= ((1.e0-math.pow(2, i-32))*(1.e0-math.pow(2, i-32)))/(1.e0-math.pow(2, i-r))
        r = 31
        product = 1
        for i in xrange(0,r):
            product *= ((1.e0-math.pow(2, i-32))*(1.e0-math.pow(2, i-32)))/(1.e0-math.pow(2, i-r));
        p_31 = math.pow(2, r*(32+32-r)-32*32) * product;

        p_30 = 1 - (p_32+p_31);
		
        F_32 = 0;
        F_31 = 0;

        # 计算矩阵秩
        matrix_count = 9
        for i in xrange(0,N):
            bin_str = input_str[i*32*32:(i+1)*32*32]
            # import pdb;pdb.set_trace()
            bin_num = map(lambda x:float(x),bin_str)
            bin_num = np.array(bin_num)
            bin_num.resize(32,32)
            # import pdb;pdb.set_trace()
            
            mRank = compute_rank(32,32,bin_num)
            # mRank = np.linalg.matrix_rank(bin_num.astype(np.float64),0)
            # print np.linalg.matrix_rank(bin_num.astype(np.float64),0),mRank
            if ( mRank == 32 ):
                F_32 += 1 
            if ( mRank == 31 ):
				F_31+=1;
        print F_32,F_31
        try:
            chi_squared =(math.pow(F_32 - N*p_32, 2)/(N*p_32) +
                        math.pow(F_31 - N*p_31, 2)/(N*p_31) +
                        math.pow(F_30 - N*p_30, 2)/(N*p_30));
        except:
            print len(bin_str)
		
        arg1 = -chi_squared/2.e0;
        p_value = math.exp(arg1);
    return p_value


def main():
    # input_str = open("../TestData/data.e").read(1000000)
    # print m_rank(input_str)
    # a = '0010000000100000001000000011000100110000001100010011000000110001001100010011000000110001001100010011000100110001001100010011000100110000001100000011000000110000001100010011000000110001001100000011000100110000001100000000101000100000001000000010000000110000001100010011000000110001001100010011000000110000001100000011000100110000001100010011000000110000001100000011000100110000001100010011000000110001001100010011000100110000001100010011000100110000000010100010000000100000001000000011000100110000001100000011000100110000001100010011000000110001001100000011000000110001001100010011000000110001001100000011000100110000001100010011000000110001001100010011000100110001001100010011000100001010001000000010000000100000001100000011000100110001001100010011000000110000001100000011000100110000001100010011000000110001001100010011000000110000001100000011000100110000001100000011000000110000001100000011000000110000001100010000101000100000001000000010000000110000001100000011000100110001001100010011000000110000001100010011000100110001'
    # b = map(lambda x:float(x),a)
    # b = np.array(b)
    # b.resize(32,32)
    # print compute_rank(32,32,b)

    # b = map(lambda x:float(x),a)
    # b = np.array(b)
    # b.resize(32,32)
    # print b
    print np.linalg.matrix_rank(b.astype(np.float64),0)
    # # a = "01011001001010101101"
    # a = np.array([
    #     [0,1,0],
    #     [1,0,1],
    #     [0,1,1],
    # ])
    # print compute_rank(3,3,a)
    # print a
if __name__ == '__main__':
    main()