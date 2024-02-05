# Format String
#2 x 1  = 2
num = 90


print(f"{num}x1={num}")
print(f"{num}x2={num*2}")
print(f"{num}x3={num*3}")
print(f"{num}x10={num*10}")


b=1
print("2x{}={},{}".format(b,2*b, 3))
print("Your name is {} and you age is {} and you are this {}".format("Pramod",23,True))