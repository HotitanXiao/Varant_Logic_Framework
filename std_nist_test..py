# coding:utf-8
"""
    进行nist的标准测试
"""
import local_settings


def main():
    testdata_path = local_settings.getTestDataPath()+"2018-03/RC4/"
    filename = testdata_path+"vrc4_p[4,4,4,4]_q[1,2,3,4].char"
    input_str = open(filename,"r").read()
    for func in local_settings.nist_func_set:
        print func["func_name"],func["func"](input_str)
    

if __name__ == '__main__':
    main()