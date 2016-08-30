# -*- coding: utf-8 -*-
# 2016/8/29 14:52
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""


def log(text='excute'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('%s call %s():' % (text,func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log
def now():
    import time
    today_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(today_time)

print(now())
