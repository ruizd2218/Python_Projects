
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
    
