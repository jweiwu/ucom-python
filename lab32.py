def sample_arg_call(arg1, arg2, arg3):
    print "first=", arg1
    print "second=", arg2
    print "third=", arg3


sample_arg_call("hi", "hello", 'abc')
l1 = ['x', 'y', 'z']
sample_arg_call(*l1)
t1 = ('p', 'q')
sample_arg_call('r', *t1)
d1 = {'course': 'bdpy', 'instructor': 'Mark', 'duration': 35}
sample_arg_call(*d1)


def courseInfo(course, instructor, duration):
    print 'course name:', course
    print 'instructor name:', instructor
    print 'duration:', duration


courseInfo(**d1)
