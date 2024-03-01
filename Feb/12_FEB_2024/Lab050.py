# global in python

# Fibonacci series

# a = 10
# b = 12
# a, b = a, a+b
# print(a, b)
# 0, 1, 1, 2, 3, 5, 8,13 ,21

a, b = 0, 1
while a < 10:
    print(a, end=" | ")
    a, b = b, a + b
