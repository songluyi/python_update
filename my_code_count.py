# -*- coding: utf-8 -*-
# 2016/8/12 10:47
"""
-------------------------------------------------------------------------------
Function:   又是中文编码问题 算了留一个坑 我个人觉得这种解法还是不错的
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import glob,os,chardet
os.chdir('./2048game')
file_list=glob.glob('*.py')
for file in file_list:
    test=open(file,errors="ignore").readlines()
    print(test)