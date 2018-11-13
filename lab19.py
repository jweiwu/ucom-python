class Person:
    def __init__(self, age):
        self.age = age


p1 = Person(8)
p2 = Person(8)
print "p1 id=%s, p2 id=%s" % (hex(id(p1)), hex(id(p2)))
p3 = p1
print "p1 id=%s, p2 id=%s, p3 id=%s" % (hex(id(p1)),
                                        hex(id(p2)),
                                        hex(id(p3)))
print p1 == p3, p1 == p2
print hash(p1), hash(p2), hash(p3)
