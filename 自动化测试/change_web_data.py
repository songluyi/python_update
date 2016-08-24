# -*- coding: utf-8 -*-
# 2016/8/20 14:32
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

import os,time,re
from openpyxl import load_workbook
from selenium import webdriver

def make_data(first_string):
    result=re.findall('[A-Z]{3}',first_string)
    print(result)
    if len(result)==0:
       result.append('')
    param=result[0]
    new_s=first_string.replace(param,'')
    return param+new_s
chromedriver = "C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"#chrome所在驱动
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://ebsapptest.nerin.com:8010/OA_HTML/RF.jsp?function_id=16402&resp_id=22593&resp_appl_id=275&security_group_id=0&lang_code=ZHS&params=f9uD-Csf0yJK45k-D90P04yPVdyR11TSVV5x7p0BhzA")
driver.find_element_by_id('usernameField').send_keys('cg02')#登陆用户名
driver.find_element_by_id('passwordField').send_keys('1q2w3e4r5t')#登陆密码
driver.find_element_by_id('SubmitButton').click()
driver.find_element_by_xpath('//*[@id="N3:UpdateImageEnabled:0"]/img').click()
for i in range(4):
    driver.find_element_by_xpath('//*[@id="LifecycleDetailsPhases"]/table[1]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td[7]/a').click()
count=0
for i in range(21,490):
    print(i)
    print(count)
    first_str=driver.find_element_by_xpath('//*[@id="N31:PhaseShortName:%s"]'%count).get_attribute("value")#获取简称的value值
    second_str=make_data(first_str)
    driver.find_element_by_xpath('//*[@id="N31:PhaseShortName:%s"]'%count).clear()
    driver.find_element_by_xpath('//*[@id="N31:PhaseShortName:%s"]'%count).send_keys(second_str)
    if count==4:
        driver.find_element_by_xpath('//*[@id="LifecycleDetailsPhases"]/table[1]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td[7]/a').click()
        count=0
        time.sleep(3)
    else:
        count=count+1