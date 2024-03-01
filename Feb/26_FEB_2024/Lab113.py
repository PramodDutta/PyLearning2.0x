# Single Inheritance
# Multi Level

class GF:
    
    def __init__(self):
        print("Automatically Called when Object is created")
    
    
    name = "Pramod"
    def home(self):
        self.name2 = "Pramod"
        print("5BHK")

class Father(GF):
    def home2(self):
        print("GOA")

class Son(Father):
   def home3(self):
       print("Bangalore")

pramod = Son()
pramod.home()


