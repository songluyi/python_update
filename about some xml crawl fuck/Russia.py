# -*- coding: utf-8 -*-
# 2016/8/6 16:30
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

import xmltodict,json,requests,urllib.request
import requests,lxml
from lxml import etree
url='http://ria.ru/society/20160802/more.html?id=1473442713&date=20160802T192820&onedayonly=1'
a=str(urllib.request.urlopen(url).read())
b=a.replace("b'",'')
c=b.replace('<?xml version="1.0"?>\\n','')
c='<root>'+c+'</root>'
# print(c)

# etree_data=etree.XML(c)
# print(etree_data)
o = xmltodict.parse(c)
data=json.dumps(o)
# print(data)
lol_data=eval(data)
need_data=lol_data['root']['div']
print(type(need_data))
print(need_data)

