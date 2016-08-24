# -*- coding: utf-8 -*-
# 2016/8/23 11:19
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

# def count():
#
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#
# f1, f2, f3 = count()
# print(f1(),f2())
#这个闭包还是蛮难理解需要多多联系才能用实践
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 5):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3, f4 = count()
print(f1(),f2(),f4())