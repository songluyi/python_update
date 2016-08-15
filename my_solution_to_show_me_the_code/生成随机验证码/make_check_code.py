# -*- coding: utf-8 -*-
# 2016/8/12 12:06
"""
-------------------------------------------------------------------------------
Function:   生成随机数字加字母验证码
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
from PIL import ImageDraw,Image,ImageFont,ImageFilter
import random
#先设置宽高
width=60*4
height=60
#随机字母
def rndChar():
    if random.randint(1,10)>3:
        return chr(random.randint(60,90))
    elif random.randint(1,10)<=3:
        return chr(random.randint(48,57))
def rndColor():#背景色随机，不过颜色浅一些
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
def rndColor2():#数字颜色深一些
     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('4080.ttf', 40)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):#先生成背景
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
