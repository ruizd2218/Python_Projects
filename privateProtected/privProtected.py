#here we define a class with our encapsulated variables
class EncapNum:
    def __init__(self):
        self._protNumVar = 2145
        self.__privNumVar = 0

#here we are setting the name of our class to obj to make it easier to call
#and to make it easier to read
obj = EncapNum()
obj._protNumVar = 62 #setting our variable value from 2145 to 62. this is how we would change the value of our var
print(obj._protNumVar) #printing our var. without obj.*** we would get an error because it doesn't know what protNumVar is outside of the scope of the class

obj.__privNumVar = 1100 
print(obj.__privNumVar)




