def foo(a, b):
    return "[foo]:result=" + str(a + b)


def bar(a, b):
    return "[bar]:result=" + str(a * b)


if __name__ == '__main__':
    print foo(2, 2)
    print bar(4, 4)
