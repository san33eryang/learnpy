# -*- coding: utf-8 -*

# 增加日志功能，并返回函数

def log(func):
    def wrapper(*args,**kwargs):
        print('call %s():'% func.__name__)
        return func(*args,**kwargs)
    return wrapper

@log
def nows():
    print('2019-3-24 12:00')


# 增加日志功能，并返回函数,并解决了 nows的名字改变的情况

import functools
def log1(func):
    @ functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('call %s():'% func.__name__)
        return func(*args,**kwargs)
    return wrapper

@log1
def nows_update():
    print('2019-3-24 12:00')


# 增加日志功能，并返回函数,解决了 nows的名字改变的情况,并可自定义text

def log2(text):
    def decorator(func):
        @ functools.wraps(func)
        def wrapper(*args,**kwargs):
            print('%s %s():'% (text,func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return decorator


@log2('execute')
def nows_update2():
    print('2019-3-24 13:00')

# exercise
import time
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        start_time=time.time()
        end_time=time.time()
        use_time=end_time-start_time
        print('%s executed in %s ms'%(fn.__name__,use_time))
        return fn(*args,**kwargs)
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.1)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.5)
    return x * y * z;

print (fast(11, 22))
print (slow(11, 22,33))

f=fast(11,22)
s = slow(11, 22, 33)

if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

print('')
print('<----next part exercise2--->')
def log3(text='info'):
    def decorator(func):
        @ functools.wraps(func)
        def wrapper(*args,**kwargs):
            print('%s enter call %s():' % (text, func.__name__))
            print('begain call')
            func_result=func(*args,**kwargs)
            print('end call')
            return func_result
        return wrapper
    return decorator

@log3()
def nows_update3():
    print('2019-3-24 14:00')

if __name__=='__main__':
    nows()
    print(nows.__name__)  # 由于return 了wrapper，so 现在nows的名字是 wrapper

    print()
    nows_update()
    print(nows_update.__name__)  # 由于return 了wrapper，so 现在nows的名字是 wrapper

    print()
    nows_update2()
    print(nows_update2.__name__)  # 由于return 了wrapper，so 现在nows的名字是 wrapper

    print()
    print('<----next part exercise--->')
    nows_update3()
