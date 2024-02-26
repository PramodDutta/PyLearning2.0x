# Single Inheritance
class Father:
    __private_villa = "GOA"
    gold = 5
    def drive_car(self):
        print("Lambo")
    
    def threeBHKFlat(self):
        print("3BHK Flat")
        
    def private_vill_access(self,is_my_son):
        print(self.__private_villa)


class Son(Father):
    pass


pramod = Son()
print(pramod.gold)
pramod.drive_car()
pramod.threeBHKFlat()
# print(pramod.__private_villa)
pramod.private_vill_access(True)

mmd = Father()
mmd.drive_car()
mmd.threeBHKFlat()
mmd.gold
