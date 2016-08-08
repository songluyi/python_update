# -*- coding: utf-8 -*-
# 2016/8/8 17:05
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
from PIL import Image
img=Image.open('NO7.png')
print(img.size)
data = [img.getpixel((i, j)) for i in range(0, 609) for j in range(43, 53)]
# print(data)
row = [chr(img.getpixel((i, 43))[0]) for i in range(0, 609, 7)]
print("".join(row))
print(''.join(map(chr,[105, 110, 116, 101, 103, 114, 105, 116, 121])))