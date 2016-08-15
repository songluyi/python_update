# -*- coding: utf-8 -*-
# 2016/8/15 16:39
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

url='http://www.kekenet.com/read/201608/460164.shtml'
import requests
from lxml import etree
headers = {'Host':'www.kekenet.com',
           'Origin':'http://www.kekenet.com',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36}',
           'Referer':'http://www.kekenet.com/read/news/List_1298.shtml',
           'Upgrade-Insecure-Requests':1,
           'Cookie':'keke_read_news_pagetotal=1295; pgv_pvid=7636489960; Hm_lvt_9c68e8500a8dd6cbf338b9afc70517ec=1471237358; Hm_lpvt_9c68e8500a8dd6cbf338b9afc70517ec=1471237845; CNZZDATA1037071=cnzz_eid%3D2135797081-1471233399-%26ntime%3D1471233399'
          }

data=requests.get(url,headers)
new_data=str(data.content,'utf-8',errors='ignore')
# print(new_data)
new_html = etree.HTML(new_data)
header=new_html.xpath('//*[@id="nrtitle"]')
result=new_html.xpath("//*[contains(@id, 'en')]/p")
print(result)