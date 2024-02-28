# Multiple Inheritance

# F,M -> S

class Father:
    def father_money(self):
        return "5"
    
    def home(self):
        return "This is from the Father"


class Mother:
    def mother_money(self):
        return "2"
    
    def home(self):
        return "This is from the Mother"
        


# class Son(Father, Mother):
#     pass

class Son(Mother, Father):
    def home(self):
        return "This is from the Son"



son = Son()
print(Son.mro())
# print(son.father_money())
# print(son.mother_money())
print(son.home())
# MRO - Method Resolution Order
