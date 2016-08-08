# -*- coding: utf-8 -*-
# 2016/8/8 16:20
"""
-------------------------------------------------------------------------------
Function:   python3 运行pickle报错，这个千年老库感觉简直坑爸爸
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

import pickle

data=pickle.load(open('NO6.txt','rb'))
for each in data:
    print(each)
# with open('NO6.txt','rb') as f:
#     data=pickle.load(f)
#     print(data)