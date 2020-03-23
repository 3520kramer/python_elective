"""
implement the:

        __len__         method
        __add__         method
        __repr__        method
        __str__         method
        __setitem__     method
        __delitem__     method
"""

class Deck:

    # Initializes the class to an object, and sets the values of cards
    def __init__(self):
        self.cards = ['A', 'K', 4, 7]

    # Returns the length of the object which in this case is the length of the list of cards
    def __len__(self):
        return len(self.cards)

    # Makes it possible to add to objects 
    def __add__(self, other):
        return self.cards + other.cards
    
    # A string representation of the object, but for developers
    def __repr__(self):
        pass
        # returns the objects dictrionary state
        #return str(self.__dict__) 

        # returns the class name and the values in this case a list
        return (f'Class: {self.__class__.__name__}, Values: 'f'{self.cards!r}')

    # a string representation of the object, for the "user"
    # if not implemented calling str will call the __repr__ method 
    def __str__(self):

        # Returns string representation of object
        #return f'Cards in deck: {self.cards}'

        # Returns string representation of object but more readable
        return f'Cards in deck: {", ".join(str(x) for x in self.cards)}'

    def __setitem__(self, index, value):
        self.cards[index] = value
    
    def __getitem__(self, index):
        return self.cards[index]



deck = Deck()
deck2 = Deck()
