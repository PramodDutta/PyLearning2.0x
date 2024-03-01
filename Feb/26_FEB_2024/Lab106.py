# Encapsulation - bind the data v and methods(hide the important variables)
# Data members / Class variable -
# Functions - they are closed within a single blueprint
# Wrapping or binding the data variables with the methods

class Car:
    name = None
    # password = "123"
    # 3 different tyes of Data Members / class variables

    
    def __init__(self):
        self.public_var = "public" # Public - Anyone can access it
        self._protected_var = "protected123"
        self.__private_var = "pass@123"
        self.__password = "pass@123"
        
    def _protected_method(self):
        print("Protected!")
       
    def __private_method(self):
        print("Protected!")
        print()
    
    def printName(self):
        print("I am allowed to use the private variable becz I am in class "+self.__password)
        
xuv= Car()
xuv.printName()

# lambo= Car("Lambo")
# lambo.printName()

print(xuv.public_var)
print(xuv.__password)
print(xuv.printName())

