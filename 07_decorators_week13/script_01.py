import functools

### Returning functions example ###
def parent(num):
    def first_child():
        return 'I am the first child'

    def second_child():
        return 'i am the second child'

    # Når der returneres funktioner, behøves ingen parameter-paranteser
    if num == 1:
        # When returning  function without parantheses, we are returning the reference to the function
        return first_child
    else:
        # When returning functions with parantheses, we are returning the result of the function
        return second_child()


### Simple decorator example ###
def my_decorator(func):
    def wrapper():
        print('1')
        func()
        print('2')
    return wrapper

def in_between():
    print('1.5')

# It's here that the "decoration" really happens.
# We pass the in_between function as an argument and by not using parantheses after 
# the function name, we get a reference to the function and not just the result of calling it
in_between = my_decorator(in_between)

# Use the decorator syntax instead of writing the line as above, it does the exact same thing!
# Use a @ followed by the name of the outer function to mark it as a decorator
@my_decorator
def in_between():
    print('1.5')

# the in_between function needs to be called with parantheses to give the correct output
in_between()

### Decorator with arguments example ###
def do_twice(func):
    def wrapper1(any_argument): # inner function takes arguments in as normal
        func(any_argument)
        func(any_argument)
        # if you wan't to return something you do it here as normal
    return wrapper1

@do_twice
def greet(name):
    print(f'Hi, {name}')

@do_twice
def say_something(what_to_say):
    print(what_to_say)

# calling decorator functions with arguments
greet('Hans') 
say_something('What\'s up')

