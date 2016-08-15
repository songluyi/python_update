# -*- coding: utf-8 -*-
# 2016/8/12 14:08
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

f=open('test.txt','r',encoding='utf-8').readlines()
print(f)
f2=''.join(f)
print(eval(f2))