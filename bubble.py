# -*- coding: utf-8 -*

# 冒泡法
def rank (list):
    for i in range(1,len(list)):
        for j in range(0,len(list)-i):
            if list[j] > list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                # print list[j],list[j+1]
    print (list)


rank ([7,8,1])

# 直接排序法


sum=0
for x in range(101):
    sum=sum+x
print(sum)

s1= 75

s2= 85

r=(s2/s1-1)*100

print('小明的成绩提高了%.1f%%'%r)

print('%2d-%02d' % (3, 1))

n=1
while n<=20:
    if n>10:
        break
    print(n)
    n=n+1
print('End')