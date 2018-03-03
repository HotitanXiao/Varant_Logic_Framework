# coding:utf-8
"""
作者: H.Y
日期: 
描述: 用于测试nist的可视化工具
"""
from nist_sts_python import runs,blockFrequency,frequency,matrix,DFT,VL,\
            NonOverlappingTemplateMatchings,overlappingTemplateMatchings,\
            universal,linearComplexity,serial,approximateEntropy,cusum,randomExcursions
from matplotlib.colors import LogNorm
import numpy as np
import matplotlib.pyplot as plt
import copy
from multiprocessing import Process,Queue,Pool

func_set = [
    # {"func":runs.runs_all,"args":(None),"func_name":"runs","cache":np.array([]),"runtime":np.array([])},
    # {"func":blockFrequency.block_frequency_all,"args":(None),"func_name":"BF","cache":np.array([]),"runtime":np.array([])},
    # {"func":frequency.frequency_all,"args":(None),"func_name":"F","cache":np.array([]),"runtime":np.array([])},
    # {"func":DFT.DiscreteFourierTransform_all,"args":(None),"func_name":"DFT","cache":np.array([]),"runtime":np.array([])},
    # {"func":NonOverlappingTemplateMatchings.NonOverlappingTemplateMatchings_all,"args":(None),"func_name":"NoTM","cache":np.array([]),"runtime":np.array([])},
    # {"func":overlappingTemplateMatchings.OverlappingTemplateMatchings_all,"args":(None),"func_name":"OTM","cache":np.array([]),"runtime":np.array([])},
    # # {"func":universal.universal_all,"args":(None),"func_name":"uni","cache":np.array([])},
    # {"func":linearComplexity.linearComplexity_all,"args":(None),"func_name":"lc","cache":np.array([]),"runtime":np.array([])},
    # {"func":serial.serial_all,"args":(None),"func_name":"serial","cache":np.array([]),"runtime":np.array([])},
    # {"func":approximateEntropy.approximateEntropy_all,"args":(None),"func_name":"AE","cache":np.array([]),"runtime":np.array([])},
    # {"func":cusum.CumulativeSums_all,"args":(None),"func_name":"cusum","cache":np.array([]),"runtime":np.array([])},
    # {"func":randomExcursions.randomExcursions_all,"args":(None),"func_name":"re","cache":np.array([]),"runtime":np.array([])},
    {"func":VL.get_p_array,"args":(None),"func_name":"VL_P","cache":np.array([]),"runtime":np.array([])},
    {"func":VL.get_q_array,"args":(None),"func_name":"VL_q","cache":np.array([]),"runtime":np.array([])},
]

func_set_index={}


def call_process_func(func_info_dict):
    return func_info_dict[0]["func"](func_info_dict[1],func_info_dict[2],queue=None,func_name=func_info_dict[0]["func_name"])


def process_cache_multi_processing(input_str,coordinates):
    """
    参数: 
    输出: 
    描述: 进行并发运算，快速处理各个处理方法的值
    进行特征计算的主函数
    主要用于进行进程阻塞的
    """
    print "house-process"*10
    for i in xrange(0,len(func_set)):
        func_set_index[func_set[i]["func_name"]] = i
    print func_set_index
    func_params = []
    for i in xrange(0,len(func_set)):
        func_params.append((func_set[i],input_str,coordinates))

    p_p = []
    pool = Pool(4)
    result = pool.map(call_process_func,func_params)
    print "all cache done"
    
    for item in result:
        print func_set_index[item[1]]
        print item[1]+"has completed, output has %s" % len(item[0])
        func_set[func_set_index[item[1]]]["cache"] = np.array(item[0])


    # for i in xrange(0,len(func_set)):
    #     p_process = Process(target=func_set[i]["func"],args=(input_str,coordinates,queue,i,))
    #     p_process.daemon = True
    #     p_p.append(p_process)
    # for p in p_p:
    #     p.start()

def process_cache(input_str,coordinates,queue):
    for i in xrange(0,len(func_set)):
        print "now--processing%s" % func_set[i]["func_name"]
        func_set[i]["func"](input_str,coordinates,queue,i)


def nist_multi_plot_single(input_str,coordinates,save_path=".",**kwargs):
    """
        每个方法输出一个文件
        这里需要进行一个合并操作
        例如我当前获得的统计数据长度喂7
        [0,1,2,3,4,5,6]
        我可以对这些数据进行相应的合并操作比如说是0，1合并，2，3合并
        或者是0，2合并，1，3合并
    """
    # q = Queue()
    # 一进来就直接进行处理
    # p = Process(target=process_cache,args=(input_str,coordinates,q,))
    # p.start()
    # p.join()
    q = []

    bins = [100,100]
    plot_range = [[0,1],[0,1]]
    temp_coordinates = list(coordinates)
    # print temp_coordinates
    # import pdb;pdb.set_trace()
    # process_cache(input_str,temp_coordinates,q)
    # # print len(q)
    # for i in xrange(0,len(q)):
    #     result = q[i]
    #     func_set[result[1]]["cache"] = np.array(result[0])
    process_cache_multi_processing(input_str,temp_coordinates)

    log_file = open("log.txt","wb")
    fig = plt.gcf()
    # fig.set_size_inches(8.5*5, 5.5*5)
    
    for y in xrange(0,len(func_set)):
        # a = plt.subplot(row,col+1,(y-1)*(col+1)+x)
        # 先判断是否有缓存机制
        save_filename=save_path+"/"+func_set[y]["func_name"]
        if func_set[y]["cache"].any():
            print "has_cache %s" % func_set[y]["func_name"]
            p_array = func_set[y]["cache"]
        else:
            print "has_no_cache %s" % func_set[y]["func_name"]
            p_array = func_set[y]["func"](input_str,temp_coordinates)
            func_set[y]["cache"] = np.array(p_array)

        # 绘画单独的hist图样
        p_array = func_set[y]["cache"]
        # print type(p_array),len(p_array)
        """
            这里是数据统计部分，就是在这里进行相应的操作的
        """
        ty,tx= np.histogram(p_array,bins=np.arange(min(p_array),max(p_array)+1,1))
        # print tx,ty
        gx = list(tx[0:-1])
        gy = list(ty)
        # 进行其他的操作
        gx,gy = merge_cols(gx,gy,2)
        plt.plot(gx,gy,"o")
        # plt.hist(p_array,bins=np.arange(0,1.0,0.01))
        plt.title(func_set[y]["func_name"])
        plt.tight_layout()
        plt.savefig(save_path+"/"+func_set[y]["func_name"]+".png", dpi=100)
        print "save fig done %s" % save_filename
        plt.close()
    plt.close('all') 
    log_file.close()


def merge_cols(x,y,offsets):
    """
    参数说明：
        x,y是输入的统计结果,是包含两个部分，y轴数据和x轴数据
        offsets是进行合并的偏移量
    返回值说明：返回一个新的x,y
    功能描述：    

    """
    # 首先是判断offset是不是一个数组，如果是数组的话则需要进一步处理
    if type(offsets) == int:
        # x[index+offset] 会被删除掉
        result_list = []
        for i in xrange(0,offsets + 1):  
            
            tempx = copy.deepcopy(x)
            tempy = copy.deepcopy(y)
            if i!=0:
                # 左移位
                tempx = tempx[i:] + tempx[:i]
                tempy = tempy[i:] + tempy[:i]
            for(index,item) in enumerate(tempx):
                print index,item,offsets,len(tempx),len(tempy)
                if index + offsets >= len(tempx):
                    result_list.append((tempx,tempy))
                    break
                tempy[index] += tempy[index+offsets]
                tempy.pop(index+offsets)
                tempx.pop(index+offsets)
            else:
                result_list.append((tempx,tempy))
        print result_list
        resultx = result_list[0][0]
        resulty = [0]*len(result_list[0][1])
        for tuple_item in result_list:
            for (index, item) in enumerate(tuple_item[1]):
                resulty[index] += tuple_item[1][index]
        return resultx,resulty    
    elif type(offsets) == list or type(offsets) == tuple:
        for(index,item) in enumerate(x):
            for offset in offsets:
                # print index,item,offset,len(x),len(y)
                if index + offset >= len(x):
                    return x,y
                # print "add"
                # print y[index],y[index+offset]
                y[index] = y[index+offset] + y[index]
            # print x
            # print y
            for (t,offset) in enumerate(offsets):  
                delta = offset if t==0 else offset - offsets[t-1]               
                y.pop(index+delta)
                x.pop(index+delta)
            # print "0-"*5
            # print x,y
        return x,y  
    # 如果是一个数组
    else:
        print "error"


def close_all():
    plt.close('all')



def get_result():
    results = {}
    for item in func_set:
        new_item = {}
        new_item["func_name"] = copy.deepcopy(item["func_name"])
        new_item["cache"] = copy.deepcopy(item["cache"])
        results[new_item["func_name"]]=new_item
    return results

def clean_cache():
    """
     清空缓存的数据
    """  
    for item in func_set:
        item["cache"] = np.array([])

def main():
    a = [1,2,3,4,5,6,7]
    offsets = [1,2]
    print merge_cols(range(0,7),a,1)

if __name__ == '__main__':
    main()