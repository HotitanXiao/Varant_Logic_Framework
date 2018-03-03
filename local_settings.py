# coding:utf-8
"""
    这个配置文件主要是用于配置当前电脑的TestData的路径
"""

import platform

base_path_config = {
    "windows":"D:/TestData",
    "linux":"/home/dm007/TestData",
    "macos":""
}

def getTestDataPath():
    """
        根据当前操作系统的类型来判断
    """
    sysstr = platform.system()
    if sysstr == "Windows":
        return base_path_config.get("windows")
    elif sysstr == "Linux":
        return base_path_config.get("linux")
    else:
        return None