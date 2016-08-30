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

# url='http://www.kekenet.com/read/201608/460164.shtml'
# import requests
# from lxml import etree
# headers = {'Host':'www.kekenet.com',
#            'Origin':'http://www.kekenet.com',
#            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36}',
#            'Referer':'http://www.kekenet.com/read/news/List_1298.shtml',
#            'Upgrade-Insecure-Requests':1,
#            'Cookie':'keke_read_news_pagetotal=1295; pgv_pvid=7636489960; Hm_lvt_9c68e8500a8dd6cbf338b9afc70517ec=1471237358; Hm_lpvt_9c68e8500a8dd6cbf338b9afc70517ec=1471237845; CNZZDATA1037071=cnzz_eid%3D2135797081-1471233399-%26ntime%3D1471233399'
#           }
#
# data=requests.get(url,headers)
# new_data=str(data.content,'utf-8',errors='ignore')
# # print(new_data)
# new_html = etree.HTML(new_data)
# header=new_html.xpath('//*[@id="nrtitle"]')
# result=new_html.xpath("//*[contains(@id, 'en')]/p")
# print(result)
# import string
# s='string. With. Punctuation?'
# exclude = set(string.punctuation)
# s = ''.join(ch for ch in s if ch not in exclude)
# print(s)
# import  string,re
# s='技术服务TTD'
# result=re.findall('[A-Z]{3}',s)
# print(result)
# if len(result)==0:
#    result.append('')
# param=result[0]
# new_s=s.replace(param,'')
# print(param+new_s)
#
# s=[1,2];b=['avc']
# print(s)

# import hashlib
# src='sly'
# m2=hashlib.md5()
# m2.update(src.encode('utf-8'))
# print(type(m2))
# print(dir(m2))
# print(m2.hexdigest())
#coding=utf8
# import json
# js = json.loads('{"\u6728\u6613\u67d0\u95f2\u4eba":"中国"}')
# print(json.dumps(js))
# print(json.dumps(js,ensure_ascii=False))
# import requests
# s=requests.get('http://www.baidu.com')
# print(s.content)
# import time
# today_time=time.strftime("%H:%M:%S", time.localtime()).split(':')
# print(type(today_time[0]))

import requests
import re
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)+'/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
i=1
request = requests.get(url,headers = headers)
content = request.content.decode('utf-8')
print(content)
pattern = re.compile('&lt;h2&gt;(.*)&lt;/h2&gt;.*\n&lt;/a&gt;.*\n&lt;/div&gt;.*\n.*\n.*\n.*&lt;div class="content"&gt;.*\n.*\n(.*)\n&lt;!--.*--&gt;')
items = re.findall(pattern,content)
print(items)
for item in items:
    newitem =item[1].replace('&lt;br/&gt;','\n')
    print('这是第%d个笑话:\n ' % i)
    print('作者是：' ,item[0])
    print(newitem)
    print('\n')
    i+=1


