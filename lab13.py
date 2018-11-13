class Foo:
    def __str__(self):
        return "foo object in string format"

    def __repr__(self):
        return "foo object in repr format"


f1 = Foo()
print f1
print (f1,)
print [f1]
print {f1}
print '%s, %r' % (f1, f1)
print '{0!r}, {0!s}'.format(f1)