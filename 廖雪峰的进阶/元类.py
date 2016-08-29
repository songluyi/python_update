# -*- coding: utf-8 -*-
# 2016/8/24 14:01
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

# class Hello(object):
#     def hello(self, name='world'):
#         print('Hello, %s.' % name)
#
# s=Hello()
# print(Hello().hello())
# print(type(s))
# print(type(Hello))


def fn(self,name='world'):
    print('Hello, %s.' % name)
Hello2=type('Hello123',(object,),dict(Hello123=fn))
print(Hello2)
print(Hello2().Hello123())


#元类，能够通过其创建类再创建函数的对象
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
#
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
#
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

