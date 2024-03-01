# # Factorial
# n = 5
# 5*4*3*2*1 = 120
# n = 3
# 3*2*! => 6

number = int(input("Enter the Fac number\n"))
if number < 0:
    print("Fact")
elif number == 0:
    print("Fact - ", 1)
else:
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i

print("Fact ->>", fact)
