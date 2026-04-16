import time

def adder(*args, **kwargs):
    start = time.time()

    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
        result += _

    end = time.time()
    work_time = end - start

    return result, work_time
