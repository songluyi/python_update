# -*- coding: utf-8 -*-
# 2016/8/11 14:48
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
test=open('tj.txt').readlines()
print(test)
new_test=''.join(test)
new_test=str(new_test).replace('\n','').split(' ')
print(new_test)
data={}
for c in new_test:
    data[c]=data.get(c,0)+1
print(data)

