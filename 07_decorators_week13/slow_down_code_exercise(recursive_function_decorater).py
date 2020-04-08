"""
Create a decorator function that slows down your code by 1 second for each step. 
Call this function slowdown()

For this you should use the ‘time’ module.

When you got the ‘slowdown code’ working on this recursive function, 
try to create a more (for you) normal function that does the countdown using a loop, 
and see what happens if you decorate that function with you slowdown() function.


"""

import time


def slowdown(func):
    def wrapper(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    
    return wrapper

# This function is recursive (calling it self, and decrementing) 
@slowdown
def countdown(n):
    if not n:
        return n
    else:
        print(n)
        return countdown(n-1)


# Normal function which doesn't work with the decorater, as the for loop iterates in "one go"
@slowdown
def loop_countdown(n):
    for i in range(n,0,-1):
        print(i)

