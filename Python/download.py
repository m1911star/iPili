import urllib.request
import socket
import re
from bs4 import BeautifulSoup
import sys
import os
import time
targetDir = r"D:\load"  #文件保存路径
sleep_time = 1
def destFile(url, path):
    splits = url.split('/')
    folder = splits[splits.__len__() - 2]
    parent = url.rindex('/')
    print(url[parent + 1:].strip().split('.')[0])
    temp = url[parent + 1:].strip().split('.')[0]

    if not os.path.isdir(os.path.join(targetDir, folder)):
        os.mkdir(os.path.join(targetDir, folder))
    if not os.path.isdir(os.path.join(targetDir, folder, temp)):
        os.mkdir(os.path.join(targetDir, folder, temp))
    pos = path.rindex('/')
    t = os.path.join(targetDir, folder, temp, path[pos+1:])
    print(t)
    return t
if __name__ == "__main__":  #程序运行入口
    with open('./result.txt', 'r') as f:
        weburl = f.readline().strip()
        while weburl != '':
            webheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            req = urllib.request.Request(url=weburl, headers=webheaders)  # 构造请求报头
            webpage = urllib.request.urlopen(req)  # 发送请求报头
            contentBytes = webpage.read()
            print(contentBytes)
            soup = BeautifulSoup(contentBytes, "lxml")
            for link, t in set(re.findall(r'(http:[^\s]*?(jpg|png|gif|html|HTM))', str(contentBytes))):  # 正则表达式查找所有的图片
                print(link)
                try:
                    print(destFile(weburl, link))
                    urllib.request.urlretrieve(link, destFile(weburl, link))  # 下载图片
                except:
                    print('失败')  # 异常抛出
            time.sleep(sleep_time)
            weburl = f.readline().strip()
