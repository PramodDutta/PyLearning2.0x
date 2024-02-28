# Hierarchical Inheritance

class Father:
    def home(self):
        return "This is a Father"


class Pramod(Father):
    pass
    # def home(self):
    #     return "This is a Pramod  Home"

class BroPramod(Father):
    def home(self):
        return "This is a bicycle."


pramod = Pramod()
print(pramod.home())