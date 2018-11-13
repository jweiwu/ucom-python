print 2+3, 2-3, 2*3, 2/3
print 100%23
print 2**31
print 8**2, 8^1, 8^2,8^3, 8^4, 8^5, 8^6
print 7^1, 7^2, 7^3, 7^4, 7^5, 7^6
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
c1 = 5+3j
c2 = 4-7j

print c1+c2, c1-c2, c1*c2, c1/c2

print abs(c1), c1**2
print c1.conjugate()
print c1.real, c1.imag
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from fractions import Fraction

print Fraction(2468, 24)
print Fraction(5, 3) + Fraction(17, 6) + Fraction(21, 9)

a1=Fraction(3579, 27)
print a1.denominator, a1.numerator
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from decimal import Decimal as Dec

print Dec(2.968)
print Dec('2.968')
print Dec(2968)*Dec(0.001)-Dec(2.968)
print Dec(2968)*Dec('0.001')-Dec('2.968')