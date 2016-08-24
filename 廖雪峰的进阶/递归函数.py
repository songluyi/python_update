# -*- coding: utf-8 -*-
# 2016/8/21 19:18
"""
-------------------------------------------------------------------------------
Function:   研究递归函数
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""


# def fact(n):#会导致堆伐溢出的函数
#     if n==1:
#         return 1
#     return n * fact(n - 1)

# print(fact(1000))

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(1000))

#编译器均没有对尾递归做优化