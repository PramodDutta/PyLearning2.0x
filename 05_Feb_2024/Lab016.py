name = "batman"

print(len(name)) # len -> 1
print(name[4])
print(name[5])
#print(name[6]) # IndexError: string index out of range
print(len(name)-1)
print(name[len(name)-1])

# String - Immutability
# that can't ne changed, modify
string = "Hello"
string = "Pramod"
print(string)
#string[0] = "P" #TypeError: 'str' object does not support item assignment