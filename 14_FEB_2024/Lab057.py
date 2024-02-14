# Functions
# Block of code - which can executed
# They can return something
# The can't return -> non return

# They have parameters
# They don't parameters / arguments

# Define -> Call
def say_hello():  # No Return Type and No Parameter / Argument
    # Write the Code
    print("Hello")


say_hello()


def say_hello_arg(name):  # No Return Type and with Argument
    # Write the Code
    print("Hello", name)


say_hello_arg("pramod")


def say_hello_args(name, age):  # No Return Type and with Argument
    # Write the Code
    print("Hello", name, age)


say_hello_args("pramod", 67)
say_hello_args(123, True)


def say_hello_arg_default(name="Pramod"):  # No Return Type and with Argument
    # Write the Code
    print("Hello", name)


say_hello_arg_default()
say_hello_arg_default(name="Hitesh")
say_hello_arg_default("Amit")


def sum_number_argument_ret(a, b):
    return a + b


result = sum_number_argument_ret(3, 4)
result2 = sum_number_argument_ret("Amit", "Pramod")
result3 = sum_number_argument_ret(a=10, b=90)
# result4 = sum_number_argument_ret(a="Amit", b=90)
print(result)
print(result2)
print(result3)
