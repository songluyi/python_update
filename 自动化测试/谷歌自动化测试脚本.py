# -*- coding: utf-8 -*-
# 2016/8/18 10:00
"""
-------------------------------------------------------------------------------
Function:   谷歌自动化测试脚本
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import os,time
from selenium import webdriver
chromedriver = "C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"#chrome所在驱动
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get('http://192.168.15.95:8080/pages/management/index.html')
time.sleep(2)
driver.find_element_by_id('j_username').send_keys('100232')#袁剑平的账号
driver.find_element_by_id('j_password').send_keys('100232')#袁剑平的密码
driver.find_element_by_id('loginbutton').click()
time.sleep(3)
driver.get('http://192.168.15.95:8080/pages/management/index.html')
driver.find_element_by_xpath('//*[@id="side-menu"]/li[6]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="side-menu"]/li[6]/ul/li[2]/a').click()
driver.find_element_by_xpath('//*[@id="side-menu"]/li[6]/ul/li[2]/ul/li[2]/a').click()#点开模板管理页面
time.sleep(1)
driver.find_elements_by_xpath('//*[@id="bu_queryData"]').click()




