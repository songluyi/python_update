# -*- coding: utf-8 -*-
# 2016/8/18 10:34
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import os,time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://192.168.15.95:8080/pages/management/index.html')
time.sleep(3)
driver.maximize_window()
driver.find_element_by_id('j_username').send_keys('100413')
driver.find_element_by_id('j_password').send_keys('100413')
driver.find_element_by_id('loginbutton').click()
time.sleep(3)
driver.get('http://192.168.15.95:8080/pages/management/index.html')
driver.find_element_by_xpath('//*[@id="side-menu"]/li[6]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="side-menu"]/li[6]/ul/li[2]/a').click()
driver.find_element_by_xpath('//*[@id="side-menu"]/li[6]/ul/li[2]/ul/li[2]/a').click()#点开模板管理页面