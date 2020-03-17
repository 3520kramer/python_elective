class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def __str__(self):
        return f'Name: {self.__name}'

    @property
    def navn(self):
        return self.__name

    @navn.setter
    def navn(self, name):
        self.__name = name

#person1 = Person(name = 'Hanne', age = 12)
#person2 = Person('Jørgen', 72)

#person1.age = 15

class Test:

    def __init__(self):
        self.person = Person('Hanne', 12)
    
test = Test()

person1 = Person('Søren', 33)

accounts = [1, 2]

new_accounts = [1]



for new_account in new_accounts:
    for account in accounts:
        print(new_account)
        print(account)
        print("")
        if new_account is account:
            new_accounts.remove(new_account)
            print('remove')

print(new_accounts)

#liste.append(person1)

#if person1 in liste:
    #print("true")


