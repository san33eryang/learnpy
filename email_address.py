# -*- coding: utf-8 -*-
import re
def is_valid_email(addr):
    if re.match(r'^([0-9a-zA-Z.\_]+)@([0-9a-zA-Z\_]+.com)$', addr):
        return True

# test
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('<test1>=== all address are availble')



def name_of_email(addr):
    m = re.match(r'^<([0-9a-zA-Z\s]+)>\s[0-9a-zA-Z.\_]+@[0-9a-zA-Z]+\.[a-zA-Z]{2,3}',addr)
    n = re.match(r'^([0-9a-zA-Z]+)@[0-9a-zA-Z]+\.[a-zA-Z]{2,3}',addr)
    if m:
        return m.group(1)
    else:
        return n.group(1)
a='<Tom Paris> tom@voyager.org'
print( name_of_email(a))

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('<test2>=== all address are availble')