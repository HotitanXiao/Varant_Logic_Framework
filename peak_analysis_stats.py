# coding:utf-8

from Visualize import utils
import numpy as np

def process_all_stats(data,filename):
    """
        计算所有的的统计量
    """
    #极差
    ptp = np.ptp(data)
    #方差
    var = np.var(data)
    #标准差
    std = np.std(data)
    #变异系数
    ccor = np.mean(data) / np.std(data)
    results = "%s   |%s |%s |%s |%s |" %(filename,ptp,var,std,ccor)
    return results

def go(target_path):
    all_files = utils.list_file(target_path,".npy")
    results = []
    for filename in all_files:
        a = np.load(target_path+filename)
        oneline = process_all_stats(a,filename)
        results.append(oneline)
    
    with open(target_path+"stats.txt","wb") as out_file:
        out_file.writelines(results)

def main():
    go("")

if __name__ == '__main__':
    main()