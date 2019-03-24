# -*- coding: utf-8 -*
# 求和 -- 变量作为返回值
def sumtest(*argus):
    sum=0
    for n in argus:
        sum=sum+n
    return sum

print(sumtest(1,2,3,4))

# 求和 -- 函数作为返回值,闭包
def lazy_sum(*argus):
    def sum_result():
        sum=0
        for n in argus:
            sum=sum +n
        return sum
    return sum_result

f=lazy_sum(1,2,3,4)
print(f())

print('----->')
# 计数 -- 变量作为返回值
def count():
    fs=[]
    def f(j):
        return j*j
    for n in range(1,5):
        fs.append(f(n))
    return fs
ft1,ft2,ft3,ft4 =count()
print(ft1)
print(ft2)
print(ft3)
print(ft4)

print('----->')
# 计数 -- 函数作为返回值，闭包，因为引用了n，只有在函数调用4次后，最后返回4时，才结束
def count1():
    fs=[]
    for n in range(1,5):
        def f():
            return n*n
        fs.append(f)
    return fs
f1,f2,f3,f4=count1()
print(f1())
print(f2())
print(f3())
print(f4())

print('-----2>')
# 计数 -- 函数作为返回值，再创建了一个函数，用该函数的参数绑定了循环变量的值，无论该循坏变量后续如何更改，已绑定到的函数不变
def count2():
    fs=[]
    def f(j):
        def g():
            return j*j
        return g
    for n in range(1,5):
        fs.append(f(n))
    return fs
fc1,fc2,fc3,fc4=count2()
print(fc1())
print(fc2())
print(fc3())
print(fc4())

print('-----3>')
# 练习题,利用闭包返回一个计数函数，每次调用它返回递增整数

def createCounter():
    li=[0]
    def counter():
        li[0]+=1
        return li[0]
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

