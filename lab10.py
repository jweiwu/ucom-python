var1 = 'abcde'
var2 = ['a', 'b', 'c', 'd', 'e']
print type(var1), type(var2)
print len(var1), len(var2)
print var1[3], var2[3]
var2[0] = '*'
var2[1] = 'O'
var2[2] = '@'
print var2
#var1[0] = '*'
var2[:3] = '%'
print var2
del var2[:2]
print var2
var3 = ['a','b','c','d','e']*5
var3[:10:2]='!'*len(var3[:10:2])
print var3
var3[::3]='*'*len(var3[::3])
print var3