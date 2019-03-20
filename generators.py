
def test():
    n = 0
    for t in triangles():
        print(t)
        n = n + 1
        if n == 10:
            break




def triangles():
    i = 1
    a = [1]
    b = []

    while True:
        yield a
        i = i + 1
        for j in range(i):
            if j - 1 >= 0:
                n = a[j-1]
            else:
                n = 0

            if j < len(a):
                m = a[j]
            else:
                m = 0

            s = n + m

            b.append(s)

        a = b
        b = []


def triangles2():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] +L[i+1] for i in range(len(L) - 1)] + [1]


def frange(start,end,step):
    while start < end:
        yield start
        start +=step


if __name__ == '__main__':
    for t in frange(10,20,0.5):
        print (t)