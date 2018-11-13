sales = {"iphone6": 500, "iphone6+": 400, "iphone7": 300, "iphone7+": 200}
print sales["iphone6"]
print sales.get("htc")
sales["ipad"] = 100
print sales
print 'galaxy' in sales, 'iphone6' in sales
for i in sales:
    print 'iterate sales:', i, sales[i]
for i in sales.keys():
    print 'iterate sales.keys():', i, sales[i]
for i in sales.values():
    print 'iterate sales.values():', i
for i in sales.items():
    print type(i), i
    print i[0], i[1]

for k, v in sales.items():
    print 'product %s sold %d items' % (k, v)
sales.update({'iphone6': 550, 'ipad': 150, 'watch4': 1000})
print sales
del sales['iphone7+']
del sales['iphone6+']
print sales
