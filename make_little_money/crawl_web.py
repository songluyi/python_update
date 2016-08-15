# -*- coding: utf-8 -*-
# 2016/8/15 13:07
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
base_url='http://www.kekenet.com/read/news/List_1294.shtml'
headers = {'Host':'www.kekenet.com',
           'Origin':'http://www.kekenet.com',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36}',
           'Referer':'http://www.kekenet.com/read/news/List_1298.shtml',
           'Upgrade-Insecure-Requests':1,
           'Cookie':'keke_read_news_pagetotal=1295; pgv_pvid=7636489960; Hm_lvt_9c68e8500a8dd6cbf338b9afc70517ec=1471237358; Hm_lpvt_9c68e8500a8dd6cbf338b9afc70517ec=1471237845; CNZZDATA1037071=cnzz_eid%3D2135797081-1471233399-%26ntime%3D1471233399'
          }
def make_url_list(i):
    com_single_url='http://www.kekenet.com/read/news/List_%s.shtml'%i
    return com_single_url
def get_link_page(base_url):#获得list页面每一个新闻的url
    wb_data=requests.get(base_url,headers=headers)
    html =str(wb_data.content,'utf-8',errors='ignore')
    html = etree.HTML(html)
    result = html.xpath('//*[@id="menu-list"]/li/h2/a[2]/@href')
    return result
def get_content(single_url):#获取新闻页面的标题和内容
    # headers_diff={'Host':'www.kekenet.com',
    #                'Origin':'http://www.kekenet.com',
    #                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
    #                'Referer':'http://www.kekenet.com/read/news/List_1293.shtml',
    #                'Upgrade-Insecure-Requests':1,
    #                'Cookie':'pgv_pvid=7636489960; Hm_lvt_9c68e8500a8dd6cbf338b9afc70517ec=1471237358; Hm_lpvt_9c68e8500a8dd6cbf338b9afc70517ec=1471249243; CNZZDATA1037071=cnzz_eid%3D2135797081-1471233399-%26ntime%3D1471244200'
    #               }
    wb_data=requests.get(single_url,headers)
    html =str(wb_data.content,'utf-8',errors='ignore')
    new_html = etree.HTML(html)
    header=new_html.xpath('//*[@id="nrtitle"]')
    result=new_html.xpath('//*[@class="qh_en"]')
    print(header[0].text)
    file_name=header[0].txt+'.txt'
    print(file_name)
    with open(file_name,'w') as f:
        f.write(result)
url_list=list(map(make_url_list,[i for i in range(1200,1293)]))#先测试几十条，客户要求1200条
every_url_list=list(map(get_link_page,url_list))
new_url_list=[]
for i in every_url_list:
    new_url_list.extend(i)#这个写的比较蠢，目前先这么写，把链接列表化一下
for j in new_url_list:
    print(j)
    get_content(j)



