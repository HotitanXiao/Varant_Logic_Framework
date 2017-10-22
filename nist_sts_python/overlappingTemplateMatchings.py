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

def OverlappingTemplateMatchings_house_diy(input_str,m):
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
    M = 1032
    N = n/M
    K = 5
    
    pi = [ 0.364091, 0.185659, 0.139381, 0.100571, 0.0704323, 0.139865 ]



    var_lambda = (M-m+1)/pow(2, m);
    varWj = M*(1.0/pow(2.0, m) - (2.0*m-1.0)/pow(2.0, 2.0*m));
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
        print "\t\t  NONPERIODIC TEMPLATES TEST\n"
        print "-------------------------------------------------------------------------------------\n"
        print "\t\t  COMPUTATIONAL INFORMATION\n"
        print "-------------------------------------------------------------------------------------\n"
        print "\tLAMBDA = %f\tM = %d\tN = %d\tm = %d\tn = %d\n" % (var_lambda, M, N, m, n)
        print "-------------------------------------------------------------------------------------\n"
        print "\t\tF R E Q U E N C Y\n"
        print "Template   W_1  W_2  W_3  W_4  W_5  W_6  W_7  W_8    Chi^2   P_value Assignment Index\n"
        print "-------------------------------------------------------------------------------------\n"

        # 这里是干什么的？ 
        if ( numOfTemplates[m] < MAXNUMOFTEMPLATES ):
            skip = 1;
        else:
            skip = int(numOfTemplates[m]/MAXNUMOFTEMPLATES);
        numOfTemplates[m] = int(numOfTemplates[m]/skip);
        
        sum = 0.0;
        for i in xrange(0,2):                      #/* Compute Probabilities */
            pi[i] = math.exp(-var_lambda+i*math.log(var_lambda)- math.lgamma(i+1));
            sum += pi[i];
        
        pi[0] = sum;
        for i in xrange(2,K+1):                     #/* Compute Probabilities */
            pi[i-1] = math.exp(-var_lambda+i*math.log(var_lambda)-math.lgamma(i+1));
            sum += pi[i-1];
        pi[K] = 1 - sum;

        
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
    return np.average(pvalue_array)


def OverlappingTemplateMatchings(input_str,m):
    """
    参数: 
    输出: 
    描述: 重叠模块检测，NIST改写
    """
    all_sum = 0
    p_value = 0
    varWj = 0
    chi2 = 0
    n = len(input_str)
    M = 1032
    N = n/M
    K = 5
    pi = [ 0.364091, 0.185659, 0.139381, 0.100571, 0.0704323, 0.139865 ]
    nu = [0]*6


    var_lambda = (M-m+1)/pow(2, m);

    sequence = "1"*m
    # print sequence
    varWj = M*(1.0/pow(2.0, m) - (2.0*m-1.0)/pow(2.0, 2.0*m));
    Wj = [0] * N
    if var_lambda < 0 and var_lambda==0:
        print u"参数错误"
        print "\tNONOVERLAPPING TEMPLATES TESTS ABORTED DUE TO ONE OF THE FOLLOWING : \n"
        print "\tLambda (%s) not being positive!\n" % var_lambda 
        print "\tTemplate file <%s> not existing\n" % directory
        print "\tInsufficient memory for required work space.\n"
        return  
    else:
        var_lambda = float(M-m+1)/pow(2,m);
        eta = var_lambda/2.0;
        all_sum = 0.0
        # print var_lambda,eta,
        for i in xrange(0,K):
            pi[i] = Pr(i,eta)
            all_sum += pi[i]
        pi[K] = 1 - all_sum;
        for i in xrange(0,N):
            W_obs = 0
            for j in xrange(0,M-m+1):
                # print input_str[i*M+j:i*M+j+m]
                if sequence ==  input_str[i*M+j:i*M+j+m]:
                    W_obs += 1
            if W_obs<=4:
                nu[int(W_obs)] += 1;
            else:
                nu[K] += 1
        # print nu
        all_sum = 0;
        chi2 = 0.0;        
        for i in xrange(0,K+1):
            chi2 += pow(float(nu[i]) - float(N*pi[i]), 2)/(float(N*pi[i]));
            all_sum += nu[i]                  

        p_value = igamc(K/2.0, chi2/2.0);
        return p_value


def Pr(u,eta):
    """
    参数: u是蒸熟，eta是小数
    输出: 
    描述: 计算
    """
    l = 0
    all_sum = p =.0;
    
    if ( u == 0 ):
        p = math.exp(-eta)
    else:
        all_sum = 0.0
        for l in xrange(1,u+1):
            # print "u:%s,eta:%s,l:%s" %(u,eta,l)
            all_sum += math.exp(-eta-u*math.log(2)+l*math.log(eta)-math.lgamma(l+1)+math.lgamma(u)-math.lgamma(l)-math.lgamma(u-l+1));
        p = all_sum;
    
    return p;


def OverlappingTemplateMatchings_all(input_str,coordinates,input_queue=None,func_name=None):
    """
    参数: N=8，m=4
    输出: 
    描述: 
    """ 
    result = []
    for coordinate in coordinates:
        p_value = OverlappingTemplateMatchings(input_str,4)
        result.append(p_value)
    if input_queue and func_name:
        input_queue.put((result,func_name))
    return result


def main():
    input_str = open("../TestData/data.e").read(1000000)
    # print len(input_str)
    print OverlappingTemplateMatchings(input_str,9)

if __name__ == '__main__':
    main()
