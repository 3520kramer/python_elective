
"""
-- Write a decorator that writes to a log file the time stamp of each time the add function is called

Change the log decorator to also printing the values of the argument together with the timestamp.

Print the result of the decorated function to the log file also.

Create a new function and call it printer(text) that takes a text as parameter and either returns 
or prints the text 2 times. Decorate it with your logfunction. Does it work? YES
"""

import datetime

# When we call the add function, the wrapper will also log the time in a seperate file
def my_decorator(func):
    def wrapper(*args):
        # opens a file in append mode
        file = open("log.txt", 'a')

        # calling the function with the arguments
        func(*args)

        # saving the text input and the time in a varibale for the log
        argument_and_time = f'{args} = {func(*args)} @ {datetime.datetime.now()}'

        # writes the log to the file
        file.write(f'{argument_and_time}\n')
        
        # closes the file
        file.close()
        return argument_and_time

    return wrapper

# decorator annotation
@my_decorator
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

# function which returns the text entered two times
# it works with the decorator but the output printed to the log is not ideal
@my_decorator
def printer(text):
    return f'{text} {text}'
