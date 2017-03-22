# import urllib.request
# weburl = "http://pilicreateworld.tw-blog.com/PILI/PILI67/01.HTM"
# webheader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# req = urllib.request.Request(url=weburl, headers=webheader)
# webPage=urllib.request.urlopen(req)
# data = webPage.read()
# # data = data.decode('UTF-8')
# print(data)

import urllib.request
import socket
import re
from bs4 import BeautifulSoup
import sys
import os
targetDir = r"D:\load"  #文件保存路径
origin = 'http://pilicreateworld.tw-blog.com/PILI/PILI'

def destFile(path):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    pos = path.rindex('/')
    t = os.path.join(targetDir, path[pos+1:])
    return t
if __name__ == "__main__":  #程序运行入口
        weburl = origin
        webheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = urllib.request.Request(url=weburl, headers=webheaders)  # 构造请求报头
        webpage = urllib.request.urlopen(req)  # 发送请求报头
        contentBytes = webpage.read()
        print(contentBytes)
        soup = BeautifulSoup(contentBytes, "lxml")
        result = ''
        for x in soup.findAll("a"):
            if 'HTM' in x['href']:
                result = result + "\n" + origin + x['href']
            print(x['href'])
        with open('./result.txt', 'w') as f:
            f.write(result)
    # for link, t in set(re.findall(r'(http:[^\s]*?(jpg|png|gif|html|HTM))', str(contentBytes))):  #正则表达式查找所有的图片
    #     print(link)
    #     try:
    #         urllib.request.urlretrieve(link, destFile(link)) #下载图片
    #     except:
    #         print('失败') #异常抛出