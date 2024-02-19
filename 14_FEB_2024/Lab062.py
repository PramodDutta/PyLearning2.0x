# Home - Please complete
# Fact program with the function
# default = 1

# Reverse a String

def reverse_string(str): #Pramod ->  domarP
    rev_str = ""
    for c in str:
        rev_str = c + rev_str
    return rev_str


original_str = input("Enter the String\n")
original_str = original_str.lower()
rev_str = reverse_string(original_str)
print(rev_str)

# Palindrome - str = rev_str -> p
if original_str == rev_str:
    print("Palindrome")
else:
    print("Not a Palindrome")
