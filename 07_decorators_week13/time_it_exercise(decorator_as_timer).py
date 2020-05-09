"""
Your job is, to write a decorator function that can time any piece of code
"""

import time

def timer_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return wrapper

@timer_decorator
def looping():
    for i in range(1000000):
        if i % 100000 == 0:
            print(i)

@timer_decorator
def printing():
    time.sleep(0.0001)
    print("wauw")

def print_something():
    print('Something')