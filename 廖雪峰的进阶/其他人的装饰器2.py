# -*- coding: utf-8 -*-
# 2016/8/29 15:16
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import time
class TimeRecorder:
    def __init__(self, name):
        print(name + u"开始")
        self.name = name
        self.startTime = time.time()
    def __del__(self):
        print(u"{0}结束，耗时：{1}".format(self.name, time.time() - self.startTime))

from functools import wraps
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = TimeRecorder(func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log()
def now():
    print(time.time())

now()