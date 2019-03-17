
# -*- coding: utf-8 -*

# exercise1: power m 次方
def power(n,m):
    sum = 1
    for i in range(0,m):
        sum = sum * n
        m = m -1
    return sum
print power(5,2)

def power1(n,m):
    sum=1
    while m>0:
        sum= sum *n
        m=m-1
    return sum
print power1(5,2)

# exercise2:  某数字或者字母重复出现m次- 方法1
def count(n,m):
    Li=[]
    for i in range(0,m):
        Li.append(n)
    return Li
print count('a',4)

# exercise2:  某数字或者字母重复出现m次 - 方法2
def count2(n,m):
    return n * m;
print count2 ('a',5)

# exercise2:  某数字或者字母重复出现m次 - 方法3
print('a' * 6)


# exercise3
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print 'hello,',x