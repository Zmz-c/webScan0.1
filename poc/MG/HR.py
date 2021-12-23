import sys
import requests

"""
#敏感目录检测，添加相关路径请修改SensitiveDirectory.txt文件
"""

urls = []


def hul(website):
    list = [line.strip() for line in open('txt/SensitiveDirectory.txt', 'r')]  # 读取扫描字典
    for lis in list:  # 循坏读取列表
        webs = website + lis
        u = requests.get(webs)
        if u.status_code == 200:
            urls.append("可能存在:" + webs)
    return urls
