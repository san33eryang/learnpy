
# -*- coding: utf-8 -*

# 删除奇数，只留下偶数
def is_ddd(s):
    return list(filter(lambda x:x%2==0,s ))

#去除字符串中的空格
def no_empty(s):
    return list(filter(lambda s:s and s.strip(),s))

#计算素数的方法 —— 埃氏筛法
def _odd_iter():
    n=1
    while True:       #创建奇数列，因为所有的偶数除了2，均不是素数
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x:x%n!=0

def primies():
    yield 2
    it=_odd_iter()   #初始序列  [3,5,7,9,11...]
    #print (list(it))
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)



# 联系1 ：回数， 从左往右读和从右往左读都一样。
def is_palindrome(n):
    s1=str(n)     #将数字转化为字符串
    s2=s1[::-1]    #倒置
    return s1==s2




if __name__ == '__main__':
    print(is_ddd([1,2,3,4,5,6]))
    print (no_empty(['a','1',None,'2']))
    print (is_palindrome('212'))

  # 测试:

print(list(filter(is_palindrome,range(1,20))))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:

    print('测试失败!')

for n in primies():
    if n<20:
        print(n)
    else:
        break

