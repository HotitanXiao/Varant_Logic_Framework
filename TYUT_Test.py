# coding:utf-8

from nist_sts_python import runs,blockFrequency,frequency,DFT,NonOverlappingTemplateMatchings,overlappingTemplateMatchings,\
        linearComplexity,serial,approximateEntropy,cusum,VL
from MainFrame import Segmentor,VLSequence,BitFilter
import numpy as np

func_set = [
    {"func":runs.runs_all,"args":(None),"func_name":"runs","cache":np.array([])},
    {"func":blockFrequency.block_frequency_all,"args":(None),"func_name":"BF","cache":np.array([])},
    {"func":frequency.frequency_all,"args":(None),"func_name":"F","cache":np.array([])},
    {"func":DFT.DiscreteFourierTransform_all,"args":(None),"func_name":"DFT","cache":np.array([])},
    {"func":NonOverlappingTemplateMatchings.NonOverlappingTemplateMatchings_all,"args":(None),"func_name":"NoTM","cache":np.array([])},
    {"func":overlappingTemplateMatchings.OverlappingTemplateMatchings_all,"args":(None),"func_name":"OTM","cache":np.array([])},
    # {"func":universal.universal_all,"args":(None),"func_name":"uni","cache":np.array([])},
    {"func":linearComplexity.linearComplexity_all,"args":(None),"func_name":"lc","cache":np.array([])},
    {"func":serial.serial_all,"args":(None),"func_name":"serial","cache":np.array([])},
    {"func":approximateEntropy.approximateEntropy_all,"args":(None),"func_name":"AE","cache":np.array([])},
    
    {"func":cusum.CumulativeSums_all,"args":(None),"func_name":"cusum","cache":np.array([])},
    
    {"func":VL.get_p_array,"args":(None),"func_name":"VL_P","cache":np.array([])},
    {"func":VL.get_q_array,"args":(None),"func_name":"VL_q","cache":np.array([])},
]


def main():

    input_str = open("/Users/houseyoung/TestData/TYUT_8bit_AG.txt", "rb").read()
    # print len(input_str)
    segment_size = len(input_str)/10
    coordinates = Segmentor.segmentor(input_str=input_str, segment_size=segment_size,offset=segment_size)
    temp_coordinates = list(coordinates)
    queue  = []
    for i in xrange(0,len(func_set)):
        func_set[i]["func"](input_str,temp_coordinates,queue,i)

    for i in xrange(0,len(queue)):
        result = queue[i]
        func_set[result[1]]["cache"] = np.array(result[0])
    
    for func in func_set:
        print func["func_name"],func["cache"]

if __name__ == '__main__':
    main()