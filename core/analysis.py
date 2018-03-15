#-*-coding:utf-8-*-
#
#分析测试类，检测三角形的每一项是否正确
#
import gorilla

fastTriangle = gorilla.GorilaBasis()

temp = 0 #记录组合数字的
for N in xrange(2,200):
    row  =  fastTriangle.getTriangle_SingleRow(N)
    for k in xrange(1,N+2):
        temp = fastTriangle.chose(N,k-1)
        if (sum(row[k-1])!=temp): #发现不对的地方打印出来
            print False


print '测试完成'
    
