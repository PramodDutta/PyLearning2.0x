class Mul_param:
    name = None # Class Variable
    
    def print_information(self, first_name, last_name, age):
        a = 10 # Local Variable
        print("Your name is ", first_name, last_name, age)
        print(self.name)

       

obj_ref = Mul_param()
obj_ref.print_information("Amit","Sharma", 68)