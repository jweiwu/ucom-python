class Car:
    vendor = 'Lexus'
    valid = True


print Car.vendor, Car.valid

c1 = Car()
c2 = Car()
print c1.vendor, c1.vendor, Car.vendor

c1.color = 'Red'
print c1.color, c1.vendor, c1.valid

c2.capacity = 7
print c2.capacity, c2.vendor, c2.valid

Car.max = 10000
Car.vendor = 'Toyota'
print c1.max, c1.vendor, c1.valid, c2.max, c2.vendor, c2.valid
