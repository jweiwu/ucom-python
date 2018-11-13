import copy

l1 = list('ABCDE')
l2 = copy.copy(l1)
l3 = copy.deepcopy(l1)
print hex(id(l1)), hex(id(l2))
print l1, l2
l1[0] = 'a'
l2[1] = 'b'
print l1, l2
print hex(id(l1)), hex(id(l3))
print l1, l2, l3
