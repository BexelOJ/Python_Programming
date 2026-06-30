class BankAccount:
    def __init__(self):
        self._balance = 0      # protected (convention)
        self.__pin = 1234     # private (name mangling)

    def get_balance(self):
        return self._balance

    def get_pin(self):
        return self.__pin     

ba = BankAccount()
print("Balance : ", ba.get_balance())
print("Pin : ", ba.get_pin())

