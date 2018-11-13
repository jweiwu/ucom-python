r = 5
a = r * r * 3.14159265358979323846
str1 = 'a circle, with radius=%d, area is %.3f'
print str1 % (r, a)
str2 = 'a circle, with radius=%(radius)d, area is %(area).3f'
# print str2%{'radius':r, 'area':a}
print str2 % {'area': a, 'radius': r}
str3 = 'a circle, with radius={}, area is {:.3f}'
print str3.format(r, a)
str4 = 'a circle, with radius={1}, area is {0:.3f}'
print str4.format(a, r)
str5 = 'a circle, with radius={radius}, area is {area:.3f}'
print str5.format(radius=r, area=a)