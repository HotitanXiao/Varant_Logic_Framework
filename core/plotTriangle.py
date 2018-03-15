 # -*- coding: utf-8 -*-
from Gorilla import gorilla

#本文件是输出一个杨辉三角形的一行为一个三角形
#三角形的种类是有水平的和垂直的两类。
#输出方法是：
#1、水平三角形是直接将获取到的三角形的row list按行输出
#2、垂直三角形是将row list的数据的每一个list作为一个列进行输出。

########################################################################


class CreateGTNTriangel:
    """生成行三角
    形到文件中去"""
    row_list = []
    columSum = []
    outputPath = ''#输出的根路径


    def __init__(self):
        """Constructor"""
  
    def _set_root_path(self,rootPath):
        self.outputPath = rootPath
        
    def maxNumber(self, list_input):
        """获得最大数，其中List_input
        要求是那种list中有list的数据"""
        return max(max(list_input))


    def maxCellLength(self, list_input):
        """获得最大数的字符长度"""
        return len(str(self.maxNumber(list_input)))

    def find_MaxLen_Row(self,VLTriangle_Matirx):
        """找到一个编制三角一个元组中最大行"""
        row_len_max = 0
        for x in xrange(1,len(VLTriangle_Matirx)-1):
            if len(VLTriangle_Matirx[x])>row_len_max:
                row_len_max = len(VLTriangle_Matirx[x]) 

        return row_len_max    

#这个是个用于产生一个时间目录的
    def get_time(self):
         """获取当前时间，次级根目录""" 
         import time        
         return time.strftime("%y.%m.%d-%H-%M-%S")
    def _getName(self,gtntype,N):
        """生成三角形文件名
            gtntype是输出类型"""
        result = self.get_time()
        result = result+'_'+gtntype
        result = result+'_'+str(N)

        return result

    def columSum(self, OneItem):
        """三角形一行拆分后得到的图形的一列的和"""
        columeSum = {}
        columeSum[0] = 2
        for x in xrange(1, len(OneItem)-1):
            for y in xrange(0, len(OneItem[x])):
                if columeSum.has_key(y+1):
                    columeSum[y+1] += OneItem[x][y]
                else:
                    columeSum[y+1] = OneItem[x][y]
        return columeSum.values()


    def oneRow_with_Sum(self,N,fileName):
        """标准输出的
    1  [1]
    3    [3]
    3    [3]
       [1]
        [2],[6]"""
        columeSum = {}
        a = gorilla.GorilaBasis()
        output = open(self.outputPath+fileName, 'a')

        h = a.getTriangle_SingleRow(N)
        output.write('\n')
        output.write('1   '+str(h[0]).replace('L', '')+"\n")
        for x in xrange(1,len(h)-1):
            output.write(str(sum(h[x])).replace('L','')+"    "+str(h[x]).replace('L','')+"\n")
        output.write('1   '+str(h[len(h)-1]).replace('L','')+"\n")
        
        for x in xrange(1,len(h)-1):
            for y in xrange(0,len(h[x])):                
                if columeSum.has_key(y):
                    columeSum[y] += h[x][y]
                else:
                    columeSum[y] = h[x][y]
        
        output.write('   [2],'+str(columeSum.values()).replace('L','')+'\n')
        output.close()       

    def oneRow(self,N,savePath):
        """将杨辉三角的一行转换为一个三角形并保存到文件中去"""
        a  =  gorilla.GorilaBasis()
        output = open("d:\TestData\Triangle\Triangle_N.txt",'a')
        output.write(('\n'))
        h = a.getTriangle_SingleRow(N)
        output.write(str(h[0]).replace('L','')+"\n")
        for x in xrange(1,len(h)-1):
                output.write("    "+str(h[x]).replace('L','')+"\n") 
        output.write(str(h[len(h)-1]).replace('L','')+"\n")            

    def oneRow_with_Sum_verticalV3(self,spaceflag,sumFlag,N,fileName):
        """垂直输出的-带有累加和的,长度纠正的"""
        columeSum = {}
        columSum_list = []
        a  =  gorilla.GorilaBasis()
        h = a.getTriangle_SingleRow(N) #三角形的一行，拆分后的
        row_len_max = 0
        cell_len_max = 0
        fileName_suffix = fileName #文件名后缀---其实就是有没有
        #一个单元的最大长度，以此作为对其指标
        cell_len_max = len(str(max(max(h))))
        
        stdSpace = " "*cell_len_max
        #获取单行最长
        for x in xrange(1,len(h)-1):
            if len(h[x])>row_len_max:
                row_len_max = len(h[x])
    
        #计算三角形每一列的总和
        for x in xrange(1,len(h)-1):
            for y in xrange(0,len(h[x])):                
                if columeSum.has_key(y):
                    columeSum[y] += h[x][y]
                else:
                    columeSum[y] = h[x][y]
        columSum_list = columeSum.values()
        #print rowlenmax
        output = open(self.outputPath+fileName_suffix+".txt",'a')
        output.write('\n')
        if sumFlag:
            #如果需要首页累加和的话
            #先输出第列的内容到文件的第一行 
            output.write('[2]'+stdSpace+str(h[0]).replace('L','')+' '*len(h)*cell_len_max+str(h[len(h)-1])+"\n")       
        else:
            #不需要累加和的
            #先输出第列的内容到文件的第一行
            output.write(stdSpace+str(h[0]).replace('L','')+' '*len(h)*cell_len_max+str(h[len(h)-1])+"\n")                
        
        #对于文件中的每一行
        for x in xrange(0,row_len_max):
            #开始输出了，一共需要输出的行数为单列最长
            output_str=""
            space = stdSpace*(x+1) #行头空格
            for y in xrange(1,len(h)-1):            
                if x>(len(h[y])-1):
                    continue
                else:
                    output_str = output_str+"["+str(h[y][x])+"], "+" "*(cell_len_max-len(str(h[y][x])))                                                
            
            if sumFlag and N!=1:
                output.write(str(columSum_list[x])+space+output_str+"\n")
            else:
                output.write(space+output_str+"\n")
        if sumFlag:
            output.write(str(sum(columSum_list))+"\n")
        output.close()    
    def _MetaShortSeq(self,Range,fileName_suffix_input):
        """将变值三角形的每一个单独相列出来"""
        a  =  gorilla.GorilaBasis()
        index = 1
        fileName_suffix = fileName_suffix_input #文件名后缀---其实就是有没有
        #print rowlenmax
        output = open(self.outputPath+fileName_suffix+".txt",'a')
        #output.write('\n') 
        for x in xrange(1,Range):
          triangleRow = a.getTriangle_SingleRow(x)
          for ListItem in triangleRow:
            for cellItem in ListItem:
                #output.write(str(index)+"  "+str(cellItem)+"\n")
                output.write(str(cellItem)+"\n")
                index = index+1
        output.close()

    def _MetaLongSeq(self,Range,fileName_suffix_input):
        """将变值三角形安顺序输出"""
        a  =  gorilla.GorilaBasis()
         #三角形的一行，拆分后的
        row_len_max = 0
        fileName_suffix = fileName_suffix_input #文件名后缀---其实就是有没有
        #一个单元的最大长度，以此作为对其指标
       
        # print str(h)
        output = open(self.outputPath+fileName_suffix+".txt",'a')
            #先输出第列的内容到文件的第一行   
        #对于文件中的每一行
        index = 2
        for z in xrange(1,Range):
            h = a.getTriangle_SingleRow(z)
            row_len_max = self.find_MaxLen_Row(h)
            output.write('1 '+'\n'+'1 '+'\n')
            for x in xrange(0,row_len_max):
                #开始输出了，一共需要输出的行数为单列最长
                for y in xrange(1,len(h)-1):            
                    if x>(len(h[y])-1):
                        continue
                    else:
                        #output.write(str(index)+"  "+str(h[y][x])+'\n')
                        output.write(str(h[y][x])+'\n')              
                    index = index + 1                      
        output.close()    
                #如果是基数的话，最中间那行被忽略了。
        #output.write('\n') 

    def _PascalTriangle_List(self,Range,fileName_suffix_input):
        """水平投影-杨辉三角"""
        a = gorilla.GorilaBasis()
        index = 1
        fileName_suffix = fileName_suffix_input
        output = open("d:\TestData\Triangle2\Triangle_N_vertical_sum_"+fileName_suffix+".txt",'a')
        for x in xrange(1,Range):
            triangleRow = a.getTriangle_SingleRow(x)
            for ListItem in triangleRow:
                #output.write(str(index)+" "+str(sum(ListItem))+"\n")
                output.write(str(sum(ListItem))+"，")
                index = index+1
        output.close()

    def _Projection_EvenSeq(self,Range,fileName_suffix_input):
        """偶数-垂直投影"""
        a  =  gorilla.GorilaBasis()
         #三角形的一行，拆分后的
        fileName_suffix = fileName_suffix_input #文件名后缀---其实就是有没有
        #一个单元的最大长度，以此作为对其指标
        output = open("d:\TestData\Triangle2\Triangle_N_vertical_sum_"+fileName_suffix+".txt",'w')
            #先输出第列的内容到文件的第一行   
        #对于文件中的每一行
        index = 1
        for z in xrange(1,Range):
            Item = a.getTriangle_SingleRow(z)
            columSum = self.columSum(Item)
            for x in columSum:
                #output.write(str(index)+"  "+str(x)+'\n')
                output.write(str(x)+'，')
                index = index + 1        
        output.close()    
                #如果是基数的话，最中间那行被忽略了。
        #output.write('\n') 



    
#def rows():
    #a = gorilla.GorilaBasis()
    #output = open("d:\yanghuiTriangle4.txt",'w')

    #for x in xrange(1,16):
        #output.write(str(a.getTriangle_SingleRow(x))+"\n")
        #output.close()


#def oneRow(N):
    #a  =  gorilla.GorilaBasis()
    #output = open("d:\TestData\Triangle\Triangle_N.txt",'a')
    #output.write(('\n'))
    #h = a.getTriangle_SingleRow(N)
    #output.write(str(h[0]).replace('L','')+"\n")
    #for x in xrange(1,len(h)-1):
        #output.write("    "+str(h[x]).replace('L','')+"\n")
    #output.write(str(h[len(h)-1]).replace('L','')+"\n")    

#def oneRow_with_Sum(N):
    #columeSum = {}
    #a  =  gorilla.GorilaBasis()
    #output = open("d:\TestData\Triangle2\Triangle_N"+".txt",'wa')

    #h = a.getTriangle_SingleRow(N)
    #output.write("    "+str(h[0])+"\n")
    #columeSum[0] =1
    #for x in xrange(1,len(h)-1):
        #output.write(str(sum(h[x]))+"    "+str(h[x])+"\n")
    #output.write("    "+str(h[len(h)-1])+"\n")
    #output.close()


def oneRow_with_Sum(N):  
    columeSum = {}
    a  =  gorilla.GorilaBasis()
    output = open("d:\TestData\Triangle2\Triangle_N.txt",'a')

    h = a.getTriangle_SingleRow(N)
    output.write('\n')
    output.write('   '+str(h[0]).replace('L','')+"\n")
    for x in xrange(1,len(h)-1):
        output.write(str(sum(h[x])).replace('L','')+"    "+str(h[x]).replace('L','')+"\n")
    output.write('   '+str(h[len(h)-1]).replace('L','')+"\n")
    
    for x in xrange(1,len(h)-1):
        for y in xrange(0,len(h[x])):                
            if columeSum.has_key(y):
                columeSum[y] += h[x][y]
            else:
                columeSum[y] = h[x][y]
    
    output.write('   [2],'+str(columeSum.values()).replace('L','')+'\n')
    output.close()

#----------------------------------------------------------------------
def oneRow_without_Sum_vertical(flag,N):
    """垂直输出的"""
    columeSum = {}
    a  =  gorilla.GorilaBasis()
    output = open("d:\TestData\Triangle2\Triangle_N_vertical.txt",'a')

    h = a.getTriangle_SingleRow(N) #三角形的一行
    output.write('\n')
    output.write(''+str(h[0]).replace('L','')+'\t'*len(h)+str(h[len(h)-1])+"\n")#先输出第列的内容到文件的第一行
    rowlenmax=0
    #获取单行最长
    for x in xrange(1,len(h)-1):
        if len(h[x])>rowlenmax:
            rowlenmax = len(h[x])

    #计算三角形每一列的总和
    for x in xrange(1,len(h)-1):
        for y in xrange(1,len(h[x])):                
            if columeSum.has_key(y):
                columeSum[y] += h[x][y]
            else:
                columeSum[y] = h[x][y]
    
    print rowlenmax
    #对于文件中的每一行
    for x in xrange(0,rowlenmax):
        #开始输出了，一共需要输出的行数为单列最长
        output_str=""
        space = "\t"*(x+1) #行头空格
        for y in xrange(1,len(h)-1):            
            if x>(len(h[y])-1):
                continue
            else:
                output_str = output_str+"["+str(h[y][x])+"], "                                                
        output.write(space+output_str+"\n")            
    output.close()
    


#------------------------------应该是水平的----------------------------------------
def oneRow_with_Sum_verticalV3(spaceflag,sumFlag,N,fileName_suffix_input):
    """垂直输出的-带有累加和的,长度纠正的"""
    columeSum = {}
    columSum_list = []
    a  =  gorilla.GorilaBasis()
    h = a.getTriangle_SingleRow(N) #三角形的一行，拆分后的
    row_len_max = 0
    cell_len_max = 0
    fileName_suffix = fileName_suffix_input #文件名后缀---其实就是有没有
    #一个单元的最大长度，以此作为对其指标
    cell_len_max = len(str(max(max(h))))
    
    stdSpace = " "*cell_len_max
    #获取单行最长
    for x in xrange(1,len(h)-1):
        if len(h[x])>row_len_max:
            row_len_max = len(h[x])

    #计算三角形每一列的总和
    for x in xrange(1,len(h)-1):
        for y in xrange(0,len(h[x])):                
            if columeSum.has_key(y):
                columeSum[y] += h[x][y]
            else:
                columeSum[y] = h[x][y]
    columSum_list = columeSum.values()
    #print rowlenmax
    output = open("/Users/houseyoung/TestData/"+fileName_suffix+".txt",'a')
    output.write('\n')
    if sumFlag:
        #如果需要首页累加和的话
        output.write('[2]'+stdSpace+str(h[0]).replace('L','')+' '*len(h)*cell_len_max+str(h[len(h)-1])+"\n")#先输出第列的内容到文件的第一行        
    else:
        #不需要累加和的
        output.write(stdSpace+str(h[0]).replace('L','')+' '*len(h)*cell_len_max+str(h[len(h)-1])+"\n")#先输出第列的内容到文件的第一行        
        
    
    
    
    #对于文件中的每一行
    for x in xrange(0,row_len_max):
        #开始输出了，一共需要输出的行数为单列最长
        output_str=""
        space = stdSpace*(x+1) #行头空格
        for y in xrange(1,len(h)-1):            
            if x>(len(h[y])-1):
                continue
            else:
                output_str = output_str+"["+str(h[y][x])+"], "+" "*(cell_len_max-len(str(h[y][x])))                                                
        
        if sumFlag and N!=1:
            output.write(str(columSum_list[x])+space+output_str+"\n")
        else:
            output.write(space+output_str+"\n")
    if sumFlag:
        output.write(str(sum(columSum_list))+"\n")
    output.close()
#----------------------------------------------------------------------
def oneRow_with_sum_vertical_nosapce(sumflag,N,fileName_suffix_input):
    """输出结果又sum但是没有行首缩进"""
    columeSum = {}
    columSum_list = []
    a  =  gorilla.GorilaBasis()
    h = a.getTriangle_SingleRow(N) #三角形的一行，拆分后的
    row_len_max = 0
    cell_len_max = 0
    fileName_suffix = fileName_suffix_input #文件名后缀---其实就是有没有
    #一个单元的最大长度，以此作为对其指标
    cell_len_max = len(str(max(max(h))))
    
    stdSpace = " "*cell_len_max+"  "#加上两个空格
    #获取单行最长
    for x in xrange(1,len(h)-1):
        if len(h[x])>row_len_max:
            row_len_max = len(h[x])

    #计算三角形每一列的总和
    for x in xrange(1,len(h)-1):
        for y in xrange(0,len(h[x])):                
            if columeSum.has_key(y):
                columeSum[y] += h[x][y]
            else:
                columeSum[y] = h[x][y]
    columSum_list = columeSum.values()
    #print rowlenmax
    output = open("d:\TestData\Triangle2\Triangle_N_vertical_sum_"+fileName_suffix+".txt",'a')
    output.write('\n')
    #if sumFlag:
        #如果需要首页累加和的话
    output.write('[2]'*sumflag+stdSpace+str(h[0]).replace('L','')+' '*len(h)*cell_len_max+str(h[len(h)-1])+"\n")#先输出第列的内容到文件的第一行        
    #else:
        #不需要累加和的
    #    output.write(stdSpace+str(h[0]).replace('L','')+' '*len(h)*cell_len_max+str(h[len(h)-1])+"\n")#先输出第列的内容到文件的第一行        
    #对于文件中的每一行
    for x in xrange(0,row_len_max):
        #开始输出了，一共需要输出的行数为单列最长
        output_str=""
        space = " " #行头空格
        for y in xrange(1,len(h)-1):            
            if x>(len(h[y])-1):
                continue
            else:
                output_str = output_str+"["+str(h[y][x])+"], "+" "*(cell_len_max-len(str(h[y][x])))                                                
        
        if sumflag==1 and N!=1:
            output.write(str(columSum_list[x])+space*(cell_len_max-len(str(columSum_list[x]))+2)+output_str+"\n")
        else:
            output.write(space+output_str+"\n")
    if sumflag==1:
        output.write(str(sum(columSum_list))+"\n")
    output.close()    





#----------------------------------------------------------------------
def oneRow_with_Sum_verticalV2(spaceflag,sumFlag,N,fileName_suffix_input):
    """垂直输出的-带有累加和的,长度纠正的"""
    columeSum = {}
    columSum_list = []
    a  =  gorilla.GorilaBasis()
    h = a.getTriangle_SingleRow(N) #三角形的一行，拆分后的
    row_len_max = 0
    cell_len_max = 0
    stdSpace = "\t"
    fileName_suffix = fileName_suffix_input #文件名后缀---其实就是有没有
    #计算三角形每一列的总和
    for x in xrange(1,len(h)-1):
        for y in xrange(0,len(h[x])):                
            if columeSum.has_key(y):
                columeSum[y] += h[x][y]
            else:
                columeSum[y] = h[x][y]
    columSum_list = columeSum.values()
    #print rowlenmax
    output = open("/Users/houseyoung/TestData/"+fileName_suffix+".txt",'a')
    output.write('\n')
    if sumFlag:
        #如果需要首页累加和的话
        output.write('[2]'+stdSpace+str(h[0]).replace('L','')+"\n")#先输出第列的内容到文件的第一行        
    else:
        #不需要累加和的
        output.write(stdSpace+str(h[0]).replace('L','')+"\n")#先输出第列的内容到文件的第一行        
    
            
    #对于文件中的每一行
    for x in xrange(0,row_len_max):
        #开始输出了，一共需要输出的行数为单列最长
        output_str=""
        space = stdSpace*x #行头空格
        for y in xrange(1,len(h)-1):            
            if x>(len(h[y])-1):
                continue
            else:
                output_str = output_str+"["+str(h[y][x])+"],"                                        
        
        if sumFlag and N!=1:
            output.write(str(columSum_list[x])+space+output_str+"\n")
        else:
            output.write(space+output_str+"\n")
    if sumFlag:
        output.write(str(sum(columSum_list))+"\n")
    output.close()    


def VLTriangle_vertical_with_Index(Range,fileName_suffix_input):
    pass
def _createFileName(gtntype,N):
    """生成三角形文件名
        gtntype是输出类型"""
    result = "test"
    result = result+'_'+gtntype
    result = result+'_N='+str(N)
    return result

def test1(N=5):
    tr = gorilla.GorilaBasis()
    #for x in xrange(1,N):
    oneRow_with_Sum_verticalV3(spaceflag=True,sumFlag=True,N=8,fileName_suffix_input="test")
    
if __name__=='__main__':
    from timeit import Timer
    t1=Timer("test1(10)","from __main__ import test1")
    print t1.timeit(1)

     #vlt.VLTriangle_horizontal_with_Index(100,"horTest1")
    # vlt.VLTriangle_vertical_with_Index(100,"houseTest2")
    # vlt.NMTriangle_with_Index(100,"houseTest3")
    #oneRow_with_Sum_verticalV3(' ',False,4,'verticalTest2')
    # for x in xrange(1,50):
        #oneRow_with_Sum_verticalV3(False,True,x,"nospace")
        #oneRow_with_sum_vertical_nosapce(1,x,"nospace")
        #oneRow_with_Sum(x)
        #oneRow(x)
      #  oneRow_with_Sum_verticalV2(True,  True, x, "tab_space")


