# coding=utf-8
# 编写无参数的decorator，可以代替f = log()这样的临时变量f

# 这里的log只接受一个参数，因为fn只含有一个参数，所以如果factorial是多个参数，会报错
def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)

    return fn


@log
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print factorial(10)


# 这里的log可以接受多个参数，因为fn含有可变参数，所以如果factorial是多个参数，会报错
def multi_log(f):
    def fn(*args, **kwargs):
        print 'call ' + f.__name__ + '()...'
        return f(*args, **kwargs)

    return fn


@multi_log
def factorial(n, x):
    return reduce(lambda x, y: x * y, range(1, n + 1, x))


print factorial(10, 2)
