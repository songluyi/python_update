# -*- coding: utf-8 -*-
# 2016/8/29 20:12
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import time
from 喵喵.crawl_info import crawl_spider
class sms_send(object):

    def md5(self,row_str):
        import hashlib
        m2=hashlib.md5()
        m2.update(row_str.encode('utf-8'))
        return m2.hexdigest()

    def form_request(self,content):
        username='slytest'
        password='SLYSLY759'
        phone_number='15727656006'
        base_url='http://api.smsbao.com/sms?u='+username+'&p='+sms_send().md5(password)+'&m='+phone_number+'&c='+content
        return base_url

    def start_request(self):
        import requests
        content=crawl_spider().main()
        request_link=sms_send().form_request(content)
        print(request_link)
        get_back=requests.get(request_link)
        print(get_back.content)

if __name__=='__main__':

    while True:
        today_time=time.strftime("%H:%M:%S", time.localtime()).split(':')
        print(today_time)
        time.sleep(1)
        #每天早上7.00发送短信提示
        if today_time[0]=='7' and today_time[1]=='00' and today_time[2]=='00':
            sms_send().start_request()
            print('send sms successfully')





