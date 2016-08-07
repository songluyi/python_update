# -*- coding: utf-8 -*-
# 2016/8/5 15:20
"""
-------------------------------------------------------------------------------
Function:   一个图片转ascii图片的小工具
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
from PIL import Image
import argparse#这个函数也属于高阶，我会在博客介绍
def get_path():
    import os
    new_path=os.getcwd()
    FileList = []
    rootdir = new_path
    for root, subFolders, files in os.walk(rootdir):
        #排除特定的子目录
        if 'done' in subFolders:
            subFolders.remove('done')
        #查找特定扩展名的文件，只要包含.png .gif .jpg 三种主流形式
        for f in files:
            if f.find('.png') != -1 or f.find('.gif') != -1 or f.find('.jpg') != -1:
                FileList.append(os.path.join(root, f))

    for item in FileList:
        print('检测到您目录下有如下图片 请确保他们是要提交的管道等级表')
        print(item)
    return FileList
IMG_LIST = get_path()
WIDTH = 60
HEIGHT = 60
#我尝试了一下这个破玩儿如果太长，那么对于复杂的显示是很模糊的，看不清，你可以自己调试。
ascii_char = list("MMHG$OC?7>!:-;.")



# 将256灰度映射到ascii_char字符上
def get_char(r,b,g,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]#映射函数

if __name__ == '__main__':
    COUNT=1
    print('本工具自动处理脚本下所有图片文件，默认宽高均为80，可修改')
    for IMG in IMG_LIST:
        im = Image.open(IMG)
        im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
        txt = ""

        for i in range(HEIGHT):
            for j in range(WIDTH):
                txt += get_char(*im.getpixel((j,i)))#这个是值得学习的类似于*args 属于高阶学习
            txt += '\n'

        print(txt)
        with open('output'+str(COUNT)+'.txt','w') as f:
            f.write(txt)
        COUNT+=1
