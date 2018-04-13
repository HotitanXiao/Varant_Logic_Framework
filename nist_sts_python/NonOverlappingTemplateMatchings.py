# coding:utf-8
"""
作者: H.Y
日期: 
描述: 非重叠魔模块匹配

1、加载模板
2、
"""
import math
from mathUtils import *
import numpy as np
MAXNUMOFTEMPLATES = 149.

def NonOverlappingTemplateMatchings(input_str,m=8):
    """
    参数: 
    输出: 
    描述: 非重叠模块匹配
    """
    pvalue_array = []
    numOfTemplates = [0, 0, 2, 4, 6, 12, 20, 40, 74, 148, 284, 568, 1116,2232, 4424, 8848, 17622, 35244, 70340, 140680, 281076, 562152] 
    all_sum = 0
    p_value = 0
    varWj = 0
    chi2 = 0
    n = len(input_str)
    N = 8;
    M = n/N;
    K = 5
    pi = [0]*6
    # print M-m+1
    var_lambda = (M-m+1)/pow(2, m);
    varWj = M*(1.0/pow(2.0, m) - (2.0*m-1.0)/pow(2.0, 2.0*m));
    # template_file = open("./nist_sts_python/templates/template"+str(m),"r")
    template_file = open("./nist_sts_python/templates/template"+str(m),"r")
    Wj = [0] * N
    if var_lambda < 0 and var_lambda==0:
        print u"参数错误"
        print "\tNONOVERLAPPING TEMPLATES TESTS ABORTED DUE TO ONE OF THE FOLLOWING : \n"
        print "\tLambda (%s) not being positive!\n" % var_lambda 
        print "\tTemplate file <%s> not existing\n" % directory
        print "\tInsufficient memory for required work space.\n"
        return  
    else:
        # print "\t\t  NONPERIODIC TEMPLATES TEST\n"
        # print "-------------------------------------------------------------------------------------\n"
        # print "\t\t  COMPUTATIONAL INFORMATION\n"
        # print "-------------------------------------------------------------------------------------\n"
        # print "\tLAMBDA = %f\tM = %d\tN = %d\tm = %d\tn = %d\n" % (var_lambda, M, N, m, n)
        # print "-------------------------------------------------------------------------------------\n"
        # print "\t\tF R E Q U E N C Y\n"
        # print "Template   W_1  W_2  W_3  W_4  W_5  W_6  W_7  W_8    Chi^2   P_value Assignment Index\n"
        # print "-------------------------------------------------------------------------------------\n"

        # 这里是干什么的？ 
        if ( numOfTemplates[m] < MAXNUMOFTEMPLATES ):
            skip = 1;
        else:
            skip = int(numOfTemplates[m]/MAXNUMOFTEMPLATES);
        numOfTemplates[m] = int(numOfTemplates[m]/skip);
        

        all_sum = 0.0;
        for i in xrange(0,2):                      #/* Compute Probabilities */
            pi[i] = math.exp(-var_lambda+i*math.log(var_lambda)- math.lgamma(i+1));
            all_sum += pi[i];
        
        pi[0] = all_sum;
        for i in xrange(2,K+1):                     #/* Compute Probabilities */
            pi[i-1] = math.exp(-var_lambda+i*math.log(var_lambda)-math.lgamma(i+1));
            all_sum += pi[i-1];
        pi[K] = 1 - all_sum;

        
        for jj in xrange(0,min([MAXNUMOFTEMPLATES,numOfTemplates[m]])):
            all_sum = 0;
            # 加载模板 
            sequence = template_file.readline()
            sequence = sequence.replace(" ","")
            sequence = sequence.replace("\n","")
            # print sequence
            # for k in xrange(0,m):
            #     # fscanf(fp, "%d", &bit);
            #     sequence[k] = bit;
            #     sequence.append(template_file.readline())
                # fprintf(stats[TEST_NONPERIODIC], "%d", sequence[k]);
            nu = [0] * K
            for i in xrange(0,N):
                W_obs = 0
                for j in xrange(0,M-m+1):
                    # 开始滑动窗口
                    match = 1

                    if sequence == input_str[i*M+j:i*M+j+m]:
                        W_obs += 1
                        j += m-1
                Wj[i] = W_obs;
            # print Wj
            
            all_sum = 0
            chi2 = 0.0                 
            for i in xrange(0,N):
                chi2 += pow((float(Wj[i]) - var_lambda)/pow(varWj, 0.5), 2);
            p_value = igamc(N/2.0, chi2/2.0)
            pvalue_array.append(p_value)

            if isNegative(p_value) or isGreaterThanOne(p_value):
                print "\t\tWARNING:  P_VALUE IS OUT OF RANGE.\n"

            if skip > 1:
                # 从当前位置向后偏移
                fp.seek(2*m*(skip-1),1)
    return min(pvalue_array)

def NonOverlappingTemplateMatchings_all(input_str,coordinates,queue=None,func_name=None):
    """
    参数: N=8，m=4
    输出: 
    描述: 
    """ 
    print "NonOverlappingTemplateMatchings_all"
    result = []
    for coordinate in coordinates:
        test_str = input_str[coordinate[0]:coordinate[1]+1]
        p_value = NonOverlappingTemplateMatchings(test_str,4)
        result.append(p_value)
    if queue!=None and func_name!=None:
        # queue.put((result,func_name))
        queue.append((result,func_name))
    print "NonOverlappingTemplateMatchings_all end"
    return (result,func_name)


def main():
    input_str = open("../TestData/data.sha1.char").read(1024)
    # print len(input_str)
    print NonOverlappingTemplateMatchings(input_str,4)

if __name__ == '__main__':
    main()
