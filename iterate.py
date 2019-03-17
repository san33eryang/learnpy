# -*- coding: utf-8 -*
d = {'a': 1, 'b': 2, 'c': 3}


def test1():
    for key in d:
        print(key)

    for value in d.values():
        print(value)

    for key, value in d.items():
        print(key, value)

    for ch in 'zooey':
        print(ch)


def test2():
    from collections import Iterable
    print(isinstance('abc', Iterable))
    print(isinstance('123', Iterable))
    print(isinstance(123, Iterable))
    print(isinstance(['1', '2''3'], Iterable))


def test3():
    for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)

    for value in (['A', 'B', 'C']):
        print(value)


def findMinAndMax(L=[]):
    if len(L) == 0:
        return (None, None)
    return (min(L), max(L))


def test4():
    print(findMinAndMax([]))
    print(findMinAndMax([7]))
    print(findMinAndMax([1, 6]))


# testing
def test5():
    mytest = findMinAndMax
    if mytest([]) != (None, None):
        print('1测试失败!')
    elif mytest([7]) != (7, 7):
        print('2测试失败!')
    elif mytest([7, 1]) != (1, 7):
        print('3测试失败!')
    elif mytest([7, 1, 3, 9, 5]) != (1, 9):
        print('4测试失败!')
    else:
        print('5测试成功!')


def findMinAndMax2(L=[]):
    if len(L) == 0:
        return (None, None)
    if len(L) == 1:
        return (L[0], L[0])

    for i in range(1, len(L)):
        for m in range(0, len(L) - 1):
            if L[m] > L[m + 1]:
                L[m], L[m + 1] = L[m + 1], L[m]
    return (L[0], L[len(L) - 1])


def findMinAndMax3(L=[]):
    mi, ma = None, None
    print('1:'+str(L))
    for i in L:
        print('2:'+str(L))
        if mi is None or i < mi:
            mi = i
        if ma is None or i > ma:
            ma = i
    return (mi, ma)


def text():
    list1 = [1, 2, '3', '44', '555', 6, 7, 8, [9, 10]]
    print(list1)
    print(len(list1))
    for i in range(len(list1)):
        print(list1[i])

    print(list1.index('44'))


if __name__ == '__main__':
    test5()
    # findMinAndMax3()