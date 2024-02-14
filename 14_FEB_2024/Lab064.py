# Lambda Express
# To help you guys
# f(n) -> one liner in python


# def double_my_salary(salary):
#     return salary * 2
#
# result = double_my_salary(10000)
# print(result)

d_salary = lambda salary: salary * 2
print(d_salary(10))

pow_of_two = lambda num: num ** 2
print(pow_of_two(16))

sum = lambda a, b, c: a + b + c
print(sum(3, 4, c=90))

say_my_name = lambda name: print("Your name is ", name)
say_my_name("Pramod")
