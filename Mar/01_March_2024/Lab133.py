try:
    c = 10/0
except Exception as e:
    print(e)
# IndentationError
# SyntaxError
# Value Error
# Zero Div

# Exception -> Parent for the all the exception

# Good Coding and Bad
# If you know the exception which can come use that specific exception

a = int(input("Enter a number only \n"))
# Value Error -> Exp -> Good coding , You know the exception
# Exception - Bad Coding practice



try:
    a = int(input("Enter a number only \n"))
except ValueError as v:
    print(v)
except Exception as e:
    print(e)
else:
    print("Else")





