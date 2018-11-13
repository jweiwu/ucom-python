a1 = ['a', 'b', 'c', 'd', 'e']
a2 = list('PQRST')
a3 = list('ABCDE')
print type(a1), type(a2), len(a1), len(a2), a1, a2
a1.append('f')
a2.extend('U')
a3 = a3 + ['F']
print a1, a2, a3
a1.append(list('ghi'))
a2.extend(list('VWX'))
a3 = a3 + ['G','H','I']
print a1, a2, a3
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
a4 = list('qwertyuiop1234567890asdfghjklzvbnm')
a4.sort()
print a4
a4.sort(reverse=True)
print a4