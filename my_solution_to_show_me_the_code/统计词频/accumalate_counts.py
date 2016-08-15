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
from collections import OrderedDict
import string
test=open('tj.txt').readlines()
new_test=''.join(test)
new_test=str(new_test).replace('\n',' ')
# print(new_test.split(' '))
data={}
for c in new_test.split(' '):
    data[c]=data.get(c,0)+1
print(data)
data=sorted(zip(data.values(), data.keys()))
print(data)