import itertools

a1 = list('pqr')
a2 = list('ABCDE')
a3 = list('5678')
c1 = itertools.chain(a1, a2, a3)
print type(c1)
for c in c1:
    print c,
print
print "again..."
for c in c1:
    print c,
print
c2 = itertools.chain(a1, a2, a3)
l1 = [c for c in c2]
for l in l1:
    print l,

print "\nagain...\n"
for l in l1:
    print l,
print ""

l2 = 'ABCDEF'
c3 = itertools.permutations(l2, 2)
l2 = [c for c in c3]
print len(l2), [l for l in l2]
print "now print c4"
l3 = 'ABCDEF'
c4 = itertools.combinations(l3, 3)
l4 = [c for c in c4]
print len(l4), [l for l in l4]
