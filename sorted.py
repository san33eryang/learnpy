
# -*- coding: utf-8 -*

# 排序数字，或按照绝对值排序
print(sorted([-2,-6,-99,9,8]))
print(sorted([-2,-6,-99,9,8],key = abs))

#排序字母，按照大小写或忽略大小写排序
print(sorted(['bob','about','Zoo','Credit','credit']))
print(sorted(['bob','about','Zoo','Credit','credit'],key=str.lower))
print(sorted(['bob','about','Zoo','Credit','credit'],key=str.lower,reverse=True))

# 练习1 按照字母对list排序
# 方法1
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    new_list=sorted(t,key=lambda x:x[0])
    return new_list
print(by_name(L))

#方法2
def by_name1(t):
    return t[0]

print(sorted(L,key=by_name1))



# 练习2 ，按照分数排序
# 方法1
def by_score(t):
    new_list=sorted(t,key=lambda x:x[1])
    return new_list

print(by_score(L))

# 方法2
def by_score1(t):
    return t[1]
print(sorted(L,key=by_score1))