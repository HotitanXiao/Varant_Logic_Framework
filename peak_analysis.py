# coding:utf-8
"""
    观察一个序列的稳定性的，主要是通过滑动窗口进行
"""
import numpy as np
from Visualize import peack_plot
from MainFrame import VLSequence,Segmentor
from nist_sts_python import VL
import local_settings
from Visualize import utils
import copy
import VLTest
def shift_peak_analyze(basepath,filename,m,all_offset,mod="p"):
    """
        对这个东西进行循环移位，然后用滑动窗口判断他的稳定性
        输出两个数组
        peak_pos
        peak_value
        可以绘图
    """
    input_str = open(basepath+filename,"rb").read()
    results_array = []
    for offset in xrange(0,all_offset+1):
        print "shift offset = ",offset
        new_str = VLSequence.string_right_shift(input_str,offset)
        coordinates = Segmentor.segmentor(new_str,m,m)
        p_array = []
        q_array = []
        p_array,q_array = VLTest.PyVLTestForChar(new_str,m)
        # for coordinate in coordinates:
        #     p_count,q_count =  VLSequence.p_q_count(new_str[coordinate[0]:coordinate[1]+1])
        #     # print p_count,q_count
        #     q_array.append(q_count)
        #     p_array.append(p_count)
        # 统计完成
        print "offset = %s complete count now start stastic"
        q_stat_results,q_bins = np.histogram(q_array,bins=range(0,m/2+2))
        p_stat_results,p_bins = np.histogram(p_array,bins=range(0,m+2))
        results_array.append([p_stat_results,q_stat_results])
        print "offset = %s complete stats"
        
    # 完成了所有的统计了
    temp_array = np.array(results_array)
    p_stat_all = temp_array[:,0]
    q_stat_all = temp_array[:,1]
    # import pdb;pdb.set_trace()
    # print q_stat_all
    # peack_plot.peak_plot(q_stat_all,m,all_offset)
    plot_hander,peak_value,peak_pos,chi_square = peack_plot.peak_plot(p_stat_all,m,all_offset,'p')
    plot_hander.savefig(basepath+"/results/%s/%s_shift_file=%s_m=%s_offset=%s.png"%(filename,'p',filename,m,offset))
    np.save(basepath+"/results/%s/%s_shift_file=%s_m=%s_offset=%s.bin"%(filename,'p',filename,m,offset),q_stat_all)
    np.save(basepath+"/results/%s/peak_value_%s_shift_file=%s_m=%s_offset=%s.bin"%(filename,'p',filename,m,offset),peak_value)
    np.save(basepath+"/results/%s/peak_pos_%s_shift_file=%s_m=%s_offset=%s.bin"%(filename,'p',filename,m,offset),peak_pos)
    np.save(basepath+"/results/%s/chi_square_%s_shift_file=%s_m=%s_offset=%s.bin"%(filename,'p',filename,m,offset),chi_square)
    plot_hander.close("all")

    plot_hander,peak_value,peak_pos,chi_square = peack_plot.peak_plot(q_stat_all,m,all_offset,'q')
    plot_hander.savefig(basepath+"/results/%s/%s_shift_file=%s_m=%s_offset=%s.png"%(filename,'q',filename,m,offset))
    np.save(basepath+"/results/%s/%s_shift_file=%s_m=%s_offset=%s.bin"%(filename,'q',filename,m,offset),q_stat_all)
    np.save(basepath+"/results/%s/peak_pos_%s_shift_file=%s_m=%s_offset=%s.bin"%(filename,'q',filename,m,offset),peak_pos)
    np.save(basepath+"/results/%s/peak_value_%s_shift_file=%s_m=%s_offset=%s.bin"%(filename,'q',filename,m,offset),peak_value)
    np.save(basepath+"/results/%s/chi_square_%s_shift_file=%s_m=%s_offset=%s.bin"%(filename,'q',filename,m,offset),chi_square)
    plot_hander.close("all")


def xor_peak_analyze(basepath,filename,m,all_offset=0):
    """
        进行自我异或以后观察他的结果
    """
    input_str = open(basepath+filename,"rb").read()
    results_array = []
    original_string = copy.deepcopy(input_str)
    for offset in xrange(1,all_offset+1):
        print "shift offset = ",offset
        shift_str = VLSequence.string_right_shift(input_str,offset)
        p_array = []
        q_array = []
        p_array,q_array = VLTest.PyVLTowStringXorForChar(input_str1=original_string,input_str2=shift_str,m=m)
        print "offset = %s complete count now start stastic"
        q_stat_results,q_bins = np.histogram(q_array,bins=range(0,m/2+2))
        p_stat_results,p_bins = np.histogram(p_array,bins=range(0,m+2))
        results_array.append([p_stat_results,q_stat_results])
        print "offset = %s complete stats"
    temp_array = np.array(results_array)
    p_stat_all = temp_array[:,0]
    q_stat_all = temp_array[:,1]
    # import pdb;pdb.set_trace()
    # print q_stat_all 
    plot_hander = peack_plot.peak_plot(p_stat_all,m,all_offset,'p')
    plot_hander.savefig(basepath+"/results/%s/%s_xor_file=%s_m=%s_offset=%s.png"%(filename,'p',filename,m,offset))
    np.save(basepath+"/results/%s/%s_xor_file=%s_m=%s_offset=%s.bin"%(filename,'p',filename,m,offset),q_stat_all);
    plot_hander.close("all")

    plot_hander = peack_plot.peak_plot(q_stat_all,m,all_offset,'q')
    plot_hander.savefig(basepath+"/results/%s/%s_xor_file=%s_m=%s_offset=%s.png"%(filename,'q',filename,m,offset))
    np.save(basepath+"/results/%s/%s_xor_file=%s_m=%s_offset=%s.bin"%(filename,'q',filename,m,offset),q_stat_all);
    plot_hander.close("all")




def main():
    base_path = local_settings.getTestDataPath()
    # input_str = open(base_path+"/2018-03/RC4/vrc4_std.char","rb").read(10000)
    target_path = base_path + "/2018-03/Quantum/"
    file_set = utils.list_file(target_path)
    # input_str = open(base_path+"/2018-03/Quantum/TYUT.char","rb").read(1000000)
    for file_name in file_set:
    # base_path+"/2018-03/Quantum/"
        xor_peak_analyze(target_path,file_name,64,100)
        print "HOuse=------------1"
        shift_peak_analyze(target_path,file_name,64,64)
        print "HOuse=------------2"
        xor_peak_analyze(target_path,file_name,64,1000)
        print "HOuse=------------4"
        shift_peak_analyze(target_path,file_name,503,503)
        print "HOuse=------------4"

    # target_path = base_path + "/2018-03/RC4/"
    # file_set = utils.list_file(target_path)
    # # input_str = open(base_path+"/2018-03/Quantum/TYUT.char","rb").read(1000000)
    # for file_name in file_set:
    # # base_path+"/2018-03/Quantum/"
    #     xor_peak_analyze(target_path,file_name,64,100)
    #     print "HOuse=------------1"
    #     # shift_peak_analyze(target_path,file_name,64,64)
    #     # print "HOuse=------------2"

if __name__ == '__main__':
    main()