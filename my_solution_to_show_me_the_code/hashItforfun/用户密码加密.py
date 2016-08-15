# -*- coding: utf-8 -*-
# 2016/8/12 14:19
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
# import os
# from hashlib import sha256
# from hmac import HMAC
#
# def encrypt_password(password, salt=None):
#     """Hash password on the fly."""
#     if salt is None:
#         salt = os.urandom(8) # 64 bits.
#     result = password
#     for i in range(10):
#         result = HMAC(result, salt, sha256).digest()
#
#     return str(result)
#
# hashed = encrypt_password(b'admin')
# print(str(hashed).replace('b',''))

import uuid
import hashlib

def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

new_pass = input('Please enter a password: ')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = input('Now please enter the password again to check: ')
if check_password(hashed_password, old_pass):
    print('You entered the right password')
else:
    print('I am sorry but the password does not match')


