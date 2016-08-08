# -*- coding: utf-8 -*-
# 2016/8/7 19:27
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

# import string
#
# text = open('NO3.txt').read()  # 打开文件读取字符串
#
# def my_solution(text):
#     """从text中挑选出属于英文字母的字符"""
#
#     s = filter(lambda x: x in string.letters, text)
#     print(type(s))
#     print(s)
#
# if __name__ == '__main__':
#     my_solution(text)

# def is_odd(n):
#     return n % 2 == 1
#
# print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
#
# s = ''.join([line.rstrip() for line in open('NO3.txt')])
# print(s)
#
# line=open('NO3.txt')
# s=[]
# for i in line:
#     s.append(i.rstrip())
# print(''.join(s))

# s = ''.join([line.rstrip() for line in open('mess.txt')])
#
# info = dict(name= 'cold', blog='www.linuxzen.com')
# print(info.get('number',5))
# s = ''.join([line.rstrip() for line in open('NO3.txt')])
# print(s)
# import string
# a=['a','B']
# for i in a:
#     b=str.isupper(i)
#     print(b)

# s=''.join([line.rstrip() for line in open('NO4.txt')])#将txt文本全部转成str
# data=[i for i in s]
# length=len([i for i in s])
# def all_true(flag):
#     while flag is False:
#         return flag
# for i in range(3,length-3,4):
#     print(data[i])
#     test=map(str.isupper,data[i-3:i])
#     print(list(test))
    # if filter(all_true,map(str.isupper,[i-3,i-1])) and filter(all_true,map(str.isupper,[i+1,i+3])):
    #     print(i)

# a=[True,'fuck',True,False,True]
# def check_flag(data):
#     if data:
#         return data
# print(list(map(check_flag,a)))
# if False in a:
#     print('hehe')

row_id=['48976']
print(type(row_id[0]))