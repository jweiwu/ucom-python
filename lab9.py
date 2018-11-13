var1 = 'abcdefg1234567'
print type(var1), len(var1)
print var1[0], var1[13]
print var1[-1], var1[-14]
#print var1[-15]
#print var1[15]
#print var1[-5.0]
print var1[:]
print var1[:5], var1[5:]
var2 = "www.uuu.com.tw"
print var2
var3 = var2.split(".")
print var3, type(var3), var3[0]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
var1 = 'abcdefg1234567'
print 'efg' in var1, 'EFG' in var1
var2 = 'abcde'
var3 = '12345'
print var2+var3, var2*5, 5*var2
print var1[5], var1[:]
var4 = var1[0:12:2]
print var4
var5 = var1[::3]
print var5
print min(var1), max(var1)
print var1.index('2'), var1.index('g')
#print var1.index('9')
print var1.count('a'), var1.count('x')