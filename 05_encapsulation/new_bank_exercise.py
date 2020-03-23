"""
2. Bank 
In the exercise from last monday with the bank, account and customer, change the code to use properties instead of the public variables.  
The bank class should futher be change into not taking any accounts as parameters at initialization. The accouts should be added afterwards, eithers as a single account one at a time, or as a collection of accounts (many at the sametime).      
Somewhere you should change the code so that a customer only can create one account.     
The Customer class should make sure that the customer is over 18 year of age.

"""
class Bank:

    def __init__(self):
        self.__accounts_in_bank = list()
        

    def __str__(self):
        return f'Accounts: {[str(account) for account in self.__accounts_in_bank]}'

    @property
    def account(self):
        return self.__accounts_in_bank

    @account.setter
    def account(self, new_account):
        # Checks if its a list, and if it is, we iterate over the list,
        # and call the account.setter method to append each item from the list
        if isinstance(new_account, list):
            for acc in new_account:
                self.account = acc
            

        # If list is empty, then insert directly
        if len(self.__accounts_in_bank) == 0:
            self.__accounts_in_bank.append(new_account)
            print(new_account, 'added')

        # else if list is not empty and the new account is an account and not a list
        # then we can check if it's not in the __accounts_in_bank and append it
        elif isinstance(new_account, Account):
            is_duplicate = False # boolean to check if the account is a duplicate

            for account in self.__accounts_in_bank:
                # checks if the new account already is in the accounts_in_bank list
                if new_account.customer is account.customer:
                    is_duplicate = True
            
            # Then we append the new account to the list if it's not a duplicate
            if is_duplicate == False:
                self.__accounts_in_bank.append(new_account)
                print('Added')
            else:
                print('Error adding the customer to an account. The customer already has an account')
            

class Account:

    def __init__(self, account_number, customer):
        self.__account_number = account_number
        self.__customer = customer

    def __str__(self):
        return f'Account no: {self.__account_number}, {self.__customer}'

    @property
    def customer(self):
        return self.__customer

class Customer:

    def __init__(self, name, age):
        self.__name = name
        self.__age = int(age)

        if int(age) >= 18:
            self.__age = int(age)
        else:
            print("Minimum age is 18")
            while int(self.__age) < 18:
                self.__age = input('Enter new age: ')

    def __str__(self):
        return f'Name: {self.__name}, Age: {self.__age}'


# TESTING
bank = Bank()

customer1 = Customer('Hanne', 23)
customer2 = Customer('Jørgen', 53)
customer3 = Customer('Susan', 73)

account1 = Account(123, customer1)
account2 = Account(234, customer1)
account3 = Account(345, customer2)
account4 = Account(456, customer2)
account5 = Account(567, customer3)
account6 = Account(678, customer3)

bank.account = account1
bank.account = account1 # duplicate customer = not possible to add account 

print("")
print(bank) # shows only one account

liste = [account1, account3, account5, account6]
bank.account = liste

print("")
print(bank) # should print three accounts


