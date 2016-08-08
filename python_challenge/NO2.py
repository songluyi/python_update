# -*- coding: utf-8 -*-
# 2016/8/7 12:14
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import string
o=""
text="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
for each in text:
    if ord(each) >= ord('a') and ord(each) <= ord('z'):
        o += chr((ord(each) + 2 - ord('a')) % 26 + ord('a')) # 这个傻吊公式是为了解决yz 加2 溢出26个字母范围
    else:
        o += each
print(o)
