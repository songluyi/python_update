# -*- coding: utf-8 -*-
# 2016/8/7 19:13
"""
-------------------------------------------------------------------------------
Function:   这个题目的难度主要在于filter 和匿名函数的使用
            对了还有数据筛选，题目出的简直棒棒哒~
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import string
# f=open('NO3.txt').read()
# def my_solution(f):
#     s=filter(lambda x:x in string.ascii_letters,f)
#     print(s)
#     return s
# a=my_solution(f)
# print(''.join(list(a)))
occ = {}
s = ''.join([line.rstrip() for line in open('NO3.txt')])
for c in s:
    occ[c] = occ.get(c, 0) + 1  # 相同的字符，字典的值加1 厉害高手！
    print(occ[c],occ.get(c,0)+1)
    avgOC = len(s) // len(occ)
    print(avgOC)
print( ''.join([c for c in s if occ[c] < avgOC]))
