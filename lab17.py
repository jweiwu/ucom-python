age = 8
print "when age=8, age id=%s" % (hex(id(age)))
age = 10
print "when age=10, age id={!s}".format(hex(id(age)))


class Person:
    def __init__(self, age):
        self.age = age


p1 = Person(8)
print "when p1 age=8, p1 id=%s, p1.age id=%s" \
      % (hex(id(p1)), hex(id(p1.age)))
p1.age = 10
print "when p1 age=10, p1 id={!s}, p1.age id={!s}". \
    format(hex(id(p1)), hex(id(p1.age)))
