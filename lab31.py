def sample_key_arguments(fix1, fix2, **kargs):
    print "fixed part=", fix1, fix2
    for k, v in kargs.items():
        print "key=%s, value=%s" % (k, v)


sample_key_arguments("hello", "world")
sample_key_arguments("try", "with", course='bdpy', duration='35hr',
                     instructor='markho')
course1 = {'course': 'bdpy', 'duration': '35hr', 'instructor': 'markho'}
sample_key_arguments("try", 'another', **course1)
