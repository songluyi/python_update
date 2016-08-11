# -*- coding: utf-8 -*-
# 2016/8/10 12:56
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

import random,string
from functools import reduce
def make_active_code(quantity,length,sum_key):
    result=[]
    avg=int(sum_key//70)
    source=list(string.ascii_uppercase)
    source.extend(list(string.digits))
    i=0
    while len(result)< quantity:
        # print(i)
        i+=1
        key= ''
        for count in range(length):
            key += random.choice(source)
        sum_make=reduce(lambda x,y:x+y,list(map(ord,key[0:avg+1])))
        if sum_make==sum_key:
             print(key)
             print(sum_make,sum_key)
             print('符合要求 lol')
             result.append(key)
             # print(result)

    return result
def check_valid(invest_code):
    avg=int(sum_key//70)#平均值是70
    sum_check=reduce(lambda x,y:x+y,list(map(ord,invest_code[0:avg+1])))
    if sum_key==sum_check:
        return invest_code
if __name__ == "__main__":
    number = 200
    length = 15
    ascii_key=list(map(ord,str(input('please input your secret key:'))))
    sum_key=reduce(lambda x,y:x+y,ascii_key)
    code_list=make_active_code(number,length,sum_key)
    print('以下为符合项：')
    print(list(filter(check_valid,code_list)))



