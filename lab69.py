def someFunction():
    a = 1
    b = 1
    yield a
    a += b
    yield a


f1 = someFunction()
print f1.next()
print f1.next()
# print f1.next()
f2 = someFunction()
print f2.next(), f2.next()
print someFunction().next(), someFunction().next(), someFunction().next()


def someFunction2():
    x = 1
    y = 2
    z = 3
    y = yield x
    yield y + z


f21 = someFunction2()
print f21.next()
print f21.send(200)
