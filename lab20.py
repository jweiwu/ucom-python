l1 = ['A', 'B', 'C', 'D', 'E']
l2 = l1
l3 = l1[:]
l4 = list(l1)
print l1, l2, l3, l4
l1[0] = '*'
l2[1] = 'O'
l2[2] = '0'
print l1, l2, l3, l4
