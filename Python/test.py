# with open('./url.txt', 'r') as f:
#     print(f.readline())
a = r'http://pilicreateworld.tw-blog.com/PILI/PILI02/01.HTM'
print(a.split('/').__len__())
len = a.split('/').__len__()
print(a.split('/')[len - 2])