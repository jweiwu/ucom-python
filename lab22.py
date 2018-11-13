import copy

s1 = ['A', 'B']
s2 = ['C', 'D']
l1 = [s1, s2]
print l1
l2 = copy.copy(l1)
l3 = copy.deepcopy(l1)
l4 = l1
print l2, l3
l1.append(['E', 'F'])
print l1, l2
print l3, l4
l1[0][0] = 'a'
l2[1][1] = 'd'
print l1, l2
print l3, l4
