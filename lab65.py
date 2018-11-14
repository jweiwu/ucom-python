class Foo(object):
    def __init__(self):
        print('object create and need to be init...')
        self.counter = 0
        pass

    def __iter__(self):
        print("start iterator...")
        return self

    def next(self):
        if self.counter < 20:
            # print("start to iterate with counter=%d" % self.counter)
            self.counter += 1
            return self.counter
        raise StopIteration


obj1 = Foo()
for i in obj1:
    print(i)
