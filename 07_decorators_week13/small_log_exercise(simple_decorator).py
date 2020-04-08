
"""
-- Write a decorator that writes to a log file the time stamp of each time the add function is called

Change the log decorator to also printing the values of the argument together with the timestamp.

Print the result of the decorated function to the log file also.

Create a new function and call it printer(text) that takes a text as parameter and either returns 
or prints the text 2 times. Decorate it with your logfunction. Does it work? YES
"""

import datetime


def my_decorator(func):
    def wrapper(*args):
        file = open("log.txt", 'a')

        func(*args)

        argument_and_time = f'{args} = {func(*args)} @ {datetime.datetime.now()}'

        file.write(f'{argument_and_time}\n')
        
        return argument_and_time

    return wrapper

@my_decorator
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

@my_decorator
def printer(text):
    return f'{text} {text}'
