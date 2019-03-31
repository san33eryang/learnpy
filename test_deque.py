import time
from collections import deque
import random

arr=[i for i in range(1000000)]
def case1():
    for i in arr:
        j = i

def case2():
    global arr
    arr = deque(arr)
    for i in range(1000):
        j = random.randint(1,1000)
        arr.insert(j,i)

def case3():
    global arr
    for i in range(1000):
        j = random.randint(1,1000)
        arr.insert(j,i)

def calcTime(func):
    # record begin time
    begin = int(round(time.time()*1000))
    # do something
    func()
    # calculate time by (end - begin)
    end = int(round(time.time()*1000))
    print(end - begin)

if __name__ == "__main__":
    arr = [i for i in range(1000000)]
    calcTime(case1)
    arr = [i for i in range(1000000)]
    calcTime(case2)
    arr = [i for i in range(1000000)]
    calcTime(case3)