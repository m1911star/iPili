origin = 'http://pilicreateworld.tw-blog.com/PILI/PILI'
if __name__ == "__main__":  #程序运行入口
    urlSet = ''
    for x in range(1, 70):
        if x < 10:
            x = '0' + str(x)
        urlSet = urlSet + origin + str(x) + '/\n'
    with open('./url.txt', 'w') as f:
        f.write(urlSet)