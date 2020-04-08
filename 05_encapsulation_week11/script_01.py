class Person:
    def __init__(self, name, alias):
        self.name = name       # public attribute
        self.__alias = alias   # private attribute

    def who(self):
        print('name  : ', self.name)
        print('alias : ', self.__alias) 

    def foo(self):
        print('Public method')

    def __foo(self):
        print('private method')


p = Person('Flemming', 'Flemse')

print(p.name) # access public attribute
print(p._Person__alias) # access private attribute with underscore _ followed by the class name
p._Person__foo() # access private methods with underscore _ followed by the class name

# IMPORTANT TO REMEMBER THAT PROPERTIES IS USED TO MODIFY AND RETRIEVE INFORMATION ON PRIVATE VARIABLES IN OTHER CLASSES! 
# THE INTERPRETER CAN ACCESS PRIVATE VARIABLES IF WE'RE INSIDE THE CLASS

# Using properties instead of getters and setters
class Animal:
    def __init__(self, species):
        self.__species = species
    
    @property # aka. getter
    def animal(self):
        return self.__species

    @animal.setter # aka. setter
    def animal(self, species):
        self.__species = species

a = Animal('Cat')
print(a.animal) # will print the animals name by using property method
a.animal = 'Dog' # will set the animals species to be a dog, by using the setter method
 