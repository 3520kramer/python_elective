class A:
    def __init__(self, name):
        self.name = name

class B:
    def __init__(self, age):
        self.age = age

# To inherit you put the class you want to inherit from as argument in paramater
class C(A):
    def __init__(self, name):
        super().__init__(name)

# Inherit from multiple classes
class D(A,B):
    def __init__(self, name, age):
        A.__init__(self, name)
        B.__init__(self, age)