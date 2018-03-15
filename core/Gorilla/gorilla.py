# -*- coding: utf-8 -*-
# Filename: gorilla.py
from __future__ import division
import math
import matplotlib.pyplot as plt
import enum
import numpy as np
import  time


class GorilaBasis(object):
    """该类包含了基础的数学操作，获得的
    结果是杨辉三角形的某一个数字的拆分结果"""    

    def __init__(self):
        self.name='GorilaBasis'        
    def chose(self,N,n): #组合数-N选n
        """传说中的组合数学"""
        return math.factorial(N)//math.factorial(n)//math.factorial(N-n)
    
    def redundants(self,n,k,c): #一个函数,就是网上的那个
        """函数名:redundants
            参数：n 杨辉三角第n行 n>=1
                      k 第n行的第k列
                      c circular culaster
            说明:计算某个(n,k)单元"""
        if k < c:
            return 0
        if ((n-k)<k):
            return self.redundants(n,n-k,c)
        else:
            return (self.chose(abs(n-k),abs(c))*n*self.chose(abs(k-1),abs(c-1))//(n-k))
        
    
    def midProccess(self,inputArray,timeFactor=1,opcode="1111"):
        """
        函数名: midProccess
        参数: inputArray 四元np数组
                timeFactor
                opcode
        返回值: 一个nparray，是计算结果
        说明:
        """
        result = self.powerOperation(inputArray[1:5],timeFactor)
        result = result*self.operation(opcode)
        inputArray[1:5] = result
      #  print inputArray
        return inputArray
        


    def powerOperation(self,inputArray,timeFactor):
        """函数名：powerOperation
            参数：inputArray 输入的多元向量
                        timeFcator 表示次方数
            返回值：一个nparray，是计算结果
            说明：输入一个多元向量，其每个
                    元素进行次方运算    
        """
        #print inputArray
        nparry =  np.array(inputArray)
        nparry = nparry**timeFactor
        #print nparry
        return nparry


    def operation(self,opcode):
        """
        函数名：operation
        参数:
        返回值:
        说明:
        """
        #用于存放转换结果的数组
        opcodeArray = [0,0,0,0]
        if len(opcode) != 4:
            #报错
            print "error-opcode 不合法"
        else:
            for x in xrange(0,4):
                if opcode[x] == '0':
                    pass
                elif opcode[x] == '1':
                    opcodeArray[x] = 1
                elif opcode[x] == '2':
                    opcodeArray[x] = -1

        return np.array(opcodeArray)


                
        
        
    def  cRange(self,n,k): #似乎是计算某个区间的
        if ((n-k)<k):
            return self.cRange(n,n-k) #这里和C语言不一样，递归处也要return
        elif k==0:
            return [0]
        else:            
            return range(1,k+1)
    
    def createBasis(self,N,timeFactor=1,opcode="1111"):
        result = []
        for k in xrange(0,N+1):
            for c in self.cRange(N,k):
                #y=c
                y= N-k-c
                #z=c
                z = k-c
                a = self.redundants(N,k,c)
                result.append(self.midProccess(np.array([a,y,c,c,z]),timeFactor,opcode))
        return result    
    #得到一个三角形
    def getTriangle_SingleRow(self,N):
        """得到一行的所有拆分单元"""
        yanghuiTriangle = []
        for k in xrange(0,N+1):
            row = []
            #print'k'+str(k)
            for c in self.cRange(N,k):
                #print 'c'+str(c)
                row.append(self.redundants(N,k,c))
                #print row
            yanghuiTriangle.append(row)
        return yanghuiTriangle
    
    # 得到固定c的映射值
    def getCview(self,N,c):
        """
            c就是01的数量
        """
        # for i in xrange(0,)
        all_sum = 0
        for k in xrange(0,int(math.ceil(N/2.))):
            print k
            all_sum += self.redundants(N,k,c)
        all_sum *=2
        if N%2==0:
            all_sum += self.redundants(N,int(math.ceil(N/2.)),c)
        return all_sum

    # 得到固定k的映射值
    def getKview(self,N,k):
        """
            k就是1的数量
        """
        return self.chose(N,k)
    
    #使用列表推倒式的版本
    # def createBasis2(self,N):
    #     return np.array([[redundants(N,k,c),N-k-c,c,c,k-c] for k in xrange(0,N+1) for c in cRange(N,k)])

    def getMask(self,type):
        """根据输入类型生成对应的掩码"""
        pass


## End of gorrila.py
def test1(N=10):
    test = GorilaBasis()
    for x in xrange(N,N+1):
        print test.getTriangle_SingleRow(x)
if __name__ == '__main__':
    # from timeit import Timer
    # t1=Timer("test1()","from __main__ import test1")
    # print t1.timeit(100)
    test1()
    #print t1.timeit(100000)
    # test = GorilaBasis()
    # for x in xrange(0,10):
    #     print test.cRange(9,x)
