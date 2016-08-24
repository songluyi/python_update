# -*- coding: utf-8 -*-
# 2016/8/23 18:52
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import requests
from lxml import etree
import multiprocessing
headers = {'Host':'www.tianpeng.com',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36}',
           'Cookie':'uniqid=4912950bec05be78f813b30fc0b89055; __utma=172641318.1155850057.1471949774.1471949774.1471949774.1; __utmb=172641318.1.10.1471949774; __utmc=172641318; __utmz=172641318.1471949774.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1'
          }
def make_url_list(i):
    com_single_url='http://www.tianpeng.com/fuwushang/?page=%s'%i
    return com_single_url
def get_link_page(base_url):
    wb_data=requests.get(base_url,headers=headers)
    html =str(wb_data.content,'utf-8',errors='ignore')
    html = etree.HTML(html)
    result = html.xpath('/html/body/div[5]/div/div[1]/ul/li/div[1]/ul/li/a[2]/@href')
    company_name=html.xpath('/html/body/div[5]/div/div[1]/ul/li/div/div/h3/a')
    company_name=list(map(lambda x:x.text,company_name))
    city=html.xpath('/html/body/div[5]/div/div[1]/ul/li/div/p/*')
    city=list(map(lambda x:x.tail,city))
    business_scope=html.xpath('/html/body/div[5]/div/div[1]/ul/li/div/div[2]/p/em')
    business_scope=list(map(lambda x:x.text,business_scope))
    return [result,company_name,city,business_scope]#需要返回就扔进这个list

def get_shop_info(shop_url):
    wb_data=requests.get(shop_url,headers=headers)
    html =str(wb_data.content,'utf-8',errors='ignore')
    html = etree.HTML(html)
    #input your wanted xpath

if __name__ == '__main__':
    url_list=list(map(make_url_list,[i for i in range(15)]))
    all_data=list(map(get_link_page,url_list))
    print(all_data)

