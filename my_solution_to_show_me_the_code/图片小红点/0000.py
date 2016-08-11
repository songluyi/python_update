# -*- coding: utf-8 -*-
# 2016/8/10 11:19
"""
-------------------------------------------------------------------------------
Function:   show me the code first quiz
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
from PIL import Image,ImageFont,ImageDraw
image_file='图片小红点.png'
im=Image.open(image_file)
font=ImageFont.truetype('4080.ttf',46)#设置字体大小
draw=ImageDraw.Draw(im)
font_size=min(im.size)/5   #39.2
 #先设置长和宽，以图片左上角建立直角坐标系。然后数字，然后颜色然后样式。
draw.text((im.size[0]-font_size,0),'6',(256,0,0),font)
ImageDraw.Draw(im)#进行操作，写入
im.save("target.png")#保存