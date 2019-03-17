# -*- coding: utf-8 -*

# 递推函数

def f(n):
    if n <= 1:
        return n
    else:
        return f(n - 1) + f(n - 2)


li = []
for i in range(0, 3):
    li.append(f(i))
print(li)


# n！阶乘

def f1(n):
    if n <= 1:
        return 1
    return n * f1(n - 1)


print (f1(4))


# n！阶乘 优化，尾递归优化，若Return对应的 含有公式，容易引起溢出，栈会不断增加。

def f1w(n):
    return f1w_item(n, 1)


def f1w_item(n, x):
    if n <= 1:
        return x
    return f1w_item(n - 1, n * x)


print (f1w(4))


# n+n-1+n-2+...+2+1

def f2(n):
    if n <= 1:
        return 1
    return n + f2(n - 1)


print (f2(4))


# 汉诺塔 移动

def move(n, a, b, c):
    if n == 1:
        print (a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(2, 'a', 'b', 'c')

L = []
L1 = []
n = 1
m = 1
while n <= 10:
    if n % 2 != 0:
        L.append(n)
    n = n + 1
while m <= 10:
    L1.append(m)
    m = m + 2
print(L)
print(L1)

print(L[1:7])

# 去除空格
print('123456    '.replace(' ', ''))
print(' 654321 '.strip())
print(' 1 654321 1'.lstrip())
print(' 654321  1 '.rstrip())

a = '   abc def     '
def trim(s):
    if s[0] == ' ':
        s = trim(s[1:])
    if s[-1] == ' ':
        s = trim(s[:-1])
    return s


print('-->' + trim(a) + '<--')
