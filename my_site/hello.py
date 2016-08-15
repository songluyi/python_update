# -*- coding: utf-8 -*-
# 2016/8/12 17:46
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body='<hi>Hello, %s!</h1>' %(environ['PATH_INFO'][1:] or 'doubi')
    return [body.encode('utf-8')]

# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
#     return [body.encode('utf-8')]