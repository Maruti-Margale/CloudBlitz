class BankAccount:
  def __init__(self,account_number,holder_name,initial_balance):
    self.account_number = account_number
    self._holder_name = holder_name
    self.__balance = initial_balance

  def deposite(self,amount):
    if amount > 0:
      self.__balance += amount
      print(f"$ {amount} deposited. New balance : ${self.__balance}")
    else:
      print("Invalid Deposite Amount")

  def withdraw(self,amount):
    if 0 < amount <= self.__balance:
      self.__balance -= amount
      print(f"$ {amount} Withdrawn. Remaining balance : ${self.__balance}")
    else:
      print("Insufficient and Invalid Amount")

  def get_balance(self):
    return self.__balance

  def _display_holder(self):
    print(f"Account holder : {self._holder_name}")

class SavingsAccount(BankAccount):
  def __init__(self,account_number,holder_name,initial_balance,interest_rate):
    super().__init__(account_number,holder_name,initial_balance)
    self.interest_rate =interest_rate

  def apply_interest(self):
    interest = self.get_balance() * (self.interest_rate / 100)
    print(f"Applying interest : ${interest}")
    self.deposite(interest)

  def display_info(self):
    self._display_holder()
    print(f"Account Number: {self.account_number}")
    print(f"Balance : {self.get_balance()}")
    print(f"Interest rate : {self.interest_rate}")

acc = SavingsAccount(1234567889,"Maruti",1000,10)
