class Person:
    # Class Varaibles/ Instance Var
    name = "Amit"
    age = None
    
    def walk(self):
        a = 10  # Local variable
        print("Hi your name is ", self.name)
        print("Hi your age is ", self.age)
        print(a)


amit = Person()
amit.walk()

pramod  = Person()
pramod.walk()