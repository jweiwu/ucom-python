a = 5
b = 3
print 'a,b=', a, b
temp = a
a = b
b = temp
print 'a,b=', a, b
c = 4
d = 6
print 'c,d=', c, d
c, d = d, c
print 'c,d=', c, d
e = 'hello'
f = [1, 2, 3, 4, 5]
print "e,f=", e, f
e, f = f, e
print "e,f=", e, f
a = 'apple'
b = 'bosch'
c = 'casio'
d = 'dog'
a, b, c, d = d, a, b, c
print a, b, c, d