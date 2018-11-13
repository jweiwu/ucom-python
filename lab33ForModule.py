import demoModule as d

print d.foo(5, 6)
print d.bar(7, 8)

from demoModule import foo
from demoModule import bar

print foo(9, 10)
print bar(11, 12)

from demoModule import foo as f, bar as b

print f(13, 14), b(15, 16)
