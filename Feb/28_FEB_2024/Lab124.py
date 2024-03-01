# Method Overloading:
# Python does not support method overloading in the traditional sense.
# Same name of a function with different Parameter


class MathUtil(object):
    def add(self, a, b=0, c=0):
        return a + b + c
    
    # def add(self,a,b):
    #     pass
    
math = MathUtil()
op0 =  math.add(1)
op1= math.add(1, 2)
op2 = math.add(1, 2,3)