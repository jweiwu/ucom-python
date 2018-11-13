l1 = list('abcde')
s1 = 'abcde'
print l1, hex(id(l1))
print s1, hex(id(s1))
l1.append('f')
s1 += 'f'
print l1, hex(id(l1))
print s1, hex(id(s1))
