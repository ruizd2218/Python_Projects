"""
Abstraction is another fundamental aspect of Object-Oriented programming.
Data abstraction hides the complex details of items while only revealing the essential or relevant data.

Abstraction is useful for working on much larger projects when child classes may need to utilize implementation
of methods differently from its parent class and other child classes that inherit from the same parent.

Think of it like this:  You have one parent class of Payment,
then child classes need to run different payment options separately from each other,
such as Debit, Credit, Gift card, etc. They all take a payment from the customer,
but each process needs to be different according to how the banks process them.

"""
from abc import ABC, abstractmethod
class abc(ABC):
    def number(self,num):
        print("Your number is:", num)
        @abstractmethod
        def numberSet(self, num):
            pass

class SettingNumber(abc):
    def numberSet(self, num):
        print("Your number is {} and is above 100".format(num) )

obj = SettingNumber()
obj.number("200")
obj.numberSet("200")
    
