import time

def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__, 'took', end - start, 'secs')
        return result
    return f_timer

def get_number():
    for x in range(9000000):
        yield x

@timefunc
def bigCalc():
    for x in get_number():
        i = x ^ x ^ x
    return 'Fin'

print(bigCalc())
