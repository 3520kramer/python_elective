
class Bank:
    ''' Bank holding account
    '''

    def __init__(self):
        self.accounts = list()
    

class Account:

    ''' Create a customer with name param
    >>> c.name

    '''
    def __init__(self, acc_no, cust):
        self.acc_no = acc_no
        self.cust = cust
    
class Customer:
    def __init__(self, name):
        self.name = name

# creates bank
bank = Bank()

# creates customer
customer = Customer('Flemse')

# adds new account
bank.accounts.append(Account(123, customer))

# print account number from list
print(bank.accounts[0].acc_no)