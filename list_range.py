#列表生成式
def listtest(L=[]):
    L1 = ['Hello', 'World', 18, 'Apple', '18', None]
    print([s.lower() for s in L1 if isinstance(s, str) == True])
# testing
if __name__ == '__main__':
    listtest()