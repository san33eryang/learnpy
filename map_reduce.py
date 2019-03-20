
# -*- coding: utf-8 -*

from _functools import reduce

# 方法1
def f(x,y):
    return x*10+y

def strint(s):
    digitals={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9} # 可以应用于密码加密和解码
    return digitals[s]

reduce(f,list(map(strint,'12345')))

# 方法2： 方法1基础上简化

def strint2(s):
    def f2(x,y):
        return x*10 +y
    def simple(s):
        Digitals = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}  # 可以应用于密码加密和解码
        return Digitals[s]

    return reduce(f2,list(map(simple,s)))

# 方法3： 方法2基础上简化，引入 lambda, 简化 reduce用法，可以替代reduce里的函数，直接创建。

def strint3(s):
    def simple(s):
        Digitals = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}  # 可以应用于密码加密和解码
        return Digitals[s]

    return reduce(lambda x,y:x*10+y,list(map(simple,s)))

# 练习题1
# 利用map 函数，把用户输入的不规范英文名变成首字母大写，其他小写的形式
def normalize(name):
    return (name[0].upper()+ name[1:].lower())

# 练习题2
#编写一个 prod（），接受list并求积。

def prod(L):
    return reduce(lambda x,y: x*y,L) # 相当于建立一个 def x*y

# 练习题3
# 利用map 和 reduce，编写一个str2float函数，把字符串‘123.456’转换为浮点数123.456

def str2float(s):
    s=s.replace('.','')
    def simples(s):
        Digitals={'0':0,'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9':9}
        return Digitals[s]
    return (reduce(lambda x,y:x*10+y,list(map(simples,s))))/1000


# testing
if __name__ == '__main__':
    print(reduce(f,list(map(strint,'12345'))))
    print(strint2('54321'))
    print(strint3('98765'))

    #练习题1
    L1=['adam', 'LISA', 'barT']
    L2=list(map(normalize,L1))
    print(L2)

    #练习题2
    print(prod([3,5,7,9]))
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('练习题2测试成功!')
    else:
        print('练习题2测试失败!')

    # 练习题3
    print(('%.3f' % str2float('123.456')))
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('练习题3测试成功!')
    else:
        print('练习题3测试失败!')

