class MyClass:
    
    def __init__(self):
        self.name = "Amit"
        
    def public_func(self):
        print("Public Func()")
        
    def __private_func(self):
        print("This is private")
    
    def public_fn_private(self):
        self.__private_func()
        
# Security -> Not everyone can access your variables, f(n)

        
a = MyClass()
a.public_func()
# a.__private_func() - Not allowed,