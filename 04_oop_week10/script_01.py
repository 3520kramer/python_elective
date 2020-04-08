
# god stil capitalized
class A:
    # Attributes / Variables for data
    # The data changes the state of the object
    name = 'Claus'
    gender = 'Male'

    # Initializer in python (constructor in java)
    '''
    def __init__(self, name = 33): # default value
        self.name = name
    '''

    # Overload the constructor
    # Args return a tuple of the arguments given
    def _init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        if len(args) == 2:
            self.name = args[0]
            self.age = args[1]

    # The two underscores __ tells python that it's a built in method
    # private method to print (like a tostring method in java)
    # syntax to call: object 
    def __repr__(self):
        return str(self.__dict__) # {key : value}

    # private method to print (like a tostring method in java)
    # syntax to call: str(object)
    def __str__(self):
        return self.name

    # Methods
    def add(self): # The first thing in the parameter needs to be self (kind of like 'this' in java)
        pass

# create object from class

c = A('Claus')
a = A('Anna')