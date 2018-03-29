# coding:utf-8
import VRC4FPython as vrc4



def main():
    # 密钥是houseyoung
    key = "houseyoung"
    # TODO：创建标准的rc4文件
    sbox = range(0,256)
    vrc4.PyVLRC4SaveKeyStreamToFile_Sbox(sboxArray=sbox,size=20000,key=key,fileName="d:/vrc4_std.char")
    # TODO: 创建基于NIST 非重叠模块检测的 8bit template，sbox的大小为74
    sbox = [1,3,5,7,9,11,13,15,19,21,23,25,27,29,31,\
            35,37,39,43,45,47,53,55,59,61,63,\
            67,71,75,79,83,87,91,95,103,111,127,\
            128,144,152,160,164,168,172,176,180,184,188,\
            192,194,196,200,202,208,210,212,216,218,220,\
            224,226,228,230,232,234,236,240,242,244,246,248,250,252,254]
    vrc4.PyVLRC4SaveKeyStreamToFile_Sbox(sboxArray=sbox,size=20000,key=key,fileName="d:/vrc4_nist_8bit.char")
    # TODO: 创建基于基于变值三角分布的sbox的rc4数据


if __name__ == '__main__':
    main()