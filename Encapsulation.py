class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private attribute
        self._balance = balance  # protected attribute

    def get_account_number(self):  # public method
        return self.__account_number

    def deposit(self, amount):  # public method
        self._balance += amount

    def _update_balance(self, amount):  # protected method
        self._balance += amount

    def __calculate_interest(self):  # private method
        interest = self._balance * 0.05
        self._balance += interest

account = BankAccount("123456789", 1000)
print(account.get_account_number())  # prints "123456789"
account.deposit(500)
print(account._balance)  # prints 1500

# trying to access private attribute directly will raise an AttributeError
try:
    print(account.__account_number)
except AttributeError:
    print("Error: cannot access private attribute directly")

# trying to access protected attribute directly will not raise an error
print(account._balance)  # prints 1500
