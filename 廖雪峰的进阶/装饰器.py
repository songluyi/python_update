# -*- coding: utf-8 -*-
# 2016/8/23 11:51
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

# import functools
# import time
#
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
#
# @log
# def now():
#     print(time.asctime(time.localtime(time.time())))
#
# now()
#
#
# def logger(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @logger('DEBUG')
# def today():
#     print('2015-3-25')
#
# today()
# import functools
# def log(obj):
#     if isinstance(obj, str):
#         def decorator(func):
#             @functools.wraps(func)
#             def wrapper(*args, **kw):
#                 print('begin call')
#                 if obj:
#                     print('%s %s(): ' % (obj, func.__name__))
#                 else:
#                     print('call %s(): ' % func.__name__)
#                 func(*args, **kw)
#                 print('end call')
#                 return
#             return wrapper
#         return decorator
#     else:
#         @functools.wraps(obj)
#         def wrapper(*args, **kw):
#             print('begin call')
#             print('call %s(): ' % obj.__name__)
#             obj(*args, **kw)
#             print('end call')
#             return
#         return wrapper
#
#
# @log
# def fnc():
#     print('I\'m fnc for testing log without parameter')
#
#
# @log('execute')
# def fnc2():
#     print('I\'m fnc2 for testing log with parameter')
#
#
# fnc()
# print('fnc.__name__ = %s' % fnc.__name__)
# print('----------------------------------')
# fnc2()
# print('fnc2.__name__ = %s' % fnc2.__name__)
def print_integers(values):
    def is_integer(value):
        try:
          return value == int(value)
        except:
            return False
    for v in values:
        if is_integer(v):
            print(v)
        else:
            return 'False'
s=print_integers([1,2,3,"4", "parrot", 314])
print(s)
