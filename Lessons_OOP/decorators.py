import time
import functools


def testTime(fn):
    #@functools.wraps(fn)
    def wrapped(*args, **kwargs):
        st = time.time()
        result = fn(*args)
        dt = time.time() -st
        print(f"Время работы: {dt} сек")
        return result
    return wrapped


@testTime
def node1(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


@testTime
def node2(a, b):
    while (a != 0) and (b != 0):
        if a > b:
            a = a % b
        else:
            b = b % a
    return a


if __name__ == "__main__":
    print(node1(24, 24))
    print(node2(24, 256))
