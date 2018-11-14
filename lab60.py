class myClass:
    pass


print 'myclass type is:', type(myClass)
varX1 = myClass()
print "varX1 type:", type(varX1)
print "varX1 class:", varX1.__class__
print "varX1 bases:", varX1.__class__.__bases__
print "type equal?", type(varX1) == myClass
print "type equal2?", varX1.__class__ == myClass


class myClass2(object):
    pass


print 'myclass2 type is:', type(myClass2)
varX2 = myClass2()
print "varX2 type:", type(varX2)
print "varX2 class:", varX2.__class__
print "varX2 bases:", varX2.__class__.__bases__
print "type equal?", type(varX2) == myClass2
print "type equal2?", varX2.__class__ == myClass2
