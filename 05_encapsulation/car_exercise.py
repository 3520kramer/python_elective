"""
1. Car object
Create a Car class. 
When instanciated the object should be able to take 4 attributes (Make, Model, bhp, mph).
They all 4 should be properties.

"""

class Car:

    def __init__(self, make, model, bhp, mph):
        self.__make = make # setting private variables
        self.__model = model
        self.__bhp = bhp
        self.__mph = mph
    
    def __add__(self):
        return Car(f'{self.__make} {self.__model} {self.__bhp} {self.__mph}')

    def __str__(self):
        return f'Make: {self.__make}, Model: {self.__model}, BHP: {self.__bhp}, MPH: {self.__mph}'


    @property # uses property as a getter
    def make(self):
        return self.__make

    @make.setter
    def make(self, make):
        self.__make = make

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def bhp(self):
        return self.__bhp

    @bhp.setter
    def bhp(self, bhp):
        self.__bhp = bhp
    
    @property
    def mph(self):
        return self.__mph

    @mph.setter
    def mph(self, mph):
        self.__mph = mph

    
car = Car('BMW', 'M3', '100', '100')
car.model = 'M4'