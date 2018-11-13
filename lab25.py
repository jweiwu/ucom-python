x1 = range(0, 20)
print type(x1), x1
x2 = range(0, 20, 2)
print type(x2), x2
x3 = range(0, 20, 3)
print type(x3), len(x3), x3
# pip install numpy
import numpy

a1 = numpy.arange(0, 20)
print type(a1), a1
a2 = numpy.arange(0, 20, 2)
print type(a2), a2
a3 = numpy.arange(0, 2, 0.2)
print type(a3), a3

l1 = numpy.linspace(0, 20)
print type(l1), len(l1), l1
l2 = numpy.linspace(0, 20, 10)
print type(l2), len(l2), l2
l3 = numpy.linspace(0, 20, 11)
print type(l3), len(l3), l3
