class Course:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return "[%s]%s" % (str(self.name), str(self.duration))

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.name == other.name and self.duration == other.duration

    def __hash__(self):
        return hash((self.name, self.duration))


c1 = Course("BDPY", 35)
c2 = c1
print set([c1, c2])
c3 = Course("PYOO", 35)
print set([c1, c2, c3])
c4 = Course("BDPY", 35)
print set([c1, c2, c3, c4])
