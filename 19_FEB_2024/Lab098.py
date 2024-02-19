class Cal:
    def sum(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a / b


object_ref = Cal()
result = object_ref.sum(3, 4)
object_ref.div()
object_ref.sub()
object_ref.mul()
print(result)
