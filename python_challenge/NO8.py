# -*- coding: utf-8 -*-
# 2016/8/8 18:15
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import bz2
text_1=b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
text_2=b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
hack_text_1=bz2.decompress(text_1)
hack_text_2=bz2.decompress(text_2)
print(hack_text_1,hack_text_2)
lol=bz2.compress(b'572896914')
print(lol)