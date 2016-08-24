# -*- coding: utf-8 -*-
# 2016/8/23 13:41
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
chromedriver = "C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"#chrome所在驱动
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get('http://www.innotree.cn/project_extra/detail/240.html')
r=driver.find_element_by_xpath('//*[@class="details_0629_right_div01_right01_div01_span02"]')
print(r.text)
