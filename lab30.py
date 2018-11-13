def sample_variable_arguments(fix1, fix2, *args):
    print "fixed part:", fix1, fix2
    for arg in args:
        print "variable part:", arg


sample_variable_arguments("Hello", "world")
sample_variable_arguments("Hi", "begin", "X1", "X2", "X3")
sample_variable_arguments("Hi", "begin", 100, 30, 50, 'XYZ')
l1 = [100, 30, 50, 'XYZ']
sample_variable_arguments("Hi", "begin", l1)
sample_variable_arguments("Hi list", "begin", *l1)
t1 = (100, 30, 50, 'XYZ')
sample_variable_arguments("Hi, tuple", "begin", *t1)
s1 = {100, 30, 50, 'XYZ'}
sample_variable_arguments("Hi, set", "begin", *s1)
k1 = {'course': 'BDPY', 'duration': 35}
sample_variable_arguments("Hi, dict", "begin", *k1)
