
from os import listdir
'''
有一个文件，内有20万行数据，每行数据不同字段使用||分隔，将第3列的数据筛选出来，并加以去重，然后打印
'''

fn = '20W.txt'
origin = listdir('.')
with open(fn) as f:    # 读取文件
    s = f.read()
AllData = s.strip().split('\n')     # 文件放置一个字符串内
AllString = [[j.strip() for j in i.split('||')] for i in AllData]    # 转数组
RowNum = len(AllString)      # 获取数组长度，这里应该是20W
i = 0
NewString=[] # 将第三列的数据转进新数组
for i in range(RowNum):
    string=AllString[i][2]
    NewString.append(string)
dedup_list = []   # 去重
for word in NewString:
    if not word in dedup_list:
        dedup_list.append(word)
print(dedup_list)
