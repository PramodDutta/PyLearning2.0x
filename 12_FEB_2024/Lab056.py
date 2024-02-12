def sum_of_num(a, b):
    return a + b


result = sum_of_num(3, 4)
print(result)


result = sum_of_num(22.4, 49.89)
print(result)

result = sum_of_num("Pramod", "Dutta")
print(result)


# TypeError: can only concatenate str (not "int") to str
result = sum_of_num("Pramod", 123)
print(result)
