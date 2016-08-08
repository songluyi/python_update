# -*- coding: utf-8 -*-
# 2016/8/8 15:30
"""
-------------------------------------------------------------------------------
Function:   #关于第二个bug 我就懒得管了 吧初始ID输入一下就好
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import requests,re
start_id=str(63579)
broken_url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
for i in range(0,400):
    full_url=broken_url+start_id
    data=requests.get(full_url)
    print(data.content)
    if 'Yes' in str(data.content):
        row_id=int(start_id) /  2
        start_id=str(row_id)
    else:
        row_id=re.findall('\d{1,6}',str(data.content))
        print(row_id)
        start_id=row_id[0]