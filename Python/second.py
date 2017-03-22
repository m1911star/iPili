import urllib.request
from bs4 import BeautifulSoup
if __name__ == "__main__":  #程序运行入口
    with open('./url.txt', 'r') as f:
        origin = f.readline().rstrip('\n')
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