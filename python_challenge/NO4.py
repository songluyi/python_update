# -*- coding: utf-8 -*-
# 2016/8/8 9:52
"""
-------------------------------------------------------------------------------
Function:   这个提米没搞懂为啥是九个不是七个。。。
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
s=''.join([line.rstrip() for line in open('NO4.txt')])#将txt文本全部转成str
data=[j for j in s]
length=len(data)
check_flag=[]
for i in range(3,length-3,4):
    flag=[]
    flag.extend(list(map(str.isupper,data[i-3:i])))
    flag.extend(list(map(str.isupper,data[i+1:i+4])))
    if False in flag:
        print('不符合')
    else:
        print(data[i])
        check_flag.append(data[i])
row_str=''.join(check_flag)
lol=list(filter(str.islower,check_flag))
print(''.join(lol))