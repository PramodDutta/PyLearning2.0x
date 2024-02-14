# *args and **kargs
def f1(a=1, b=1, c=1):
    return a + b + c


f1()
f1(1)
f1(1, 2)
f1(1, 2, 3)
f1(a=10, b=20, c=30)


# r = f1(c=1, a=2, b=90)
# print(r)


# *args

# def sum(a, b, c, d, e):
#     return a + b + c + d + e
#
#
# r = sum(1, 2, 3)
# r = sum(1, 2, 3, 4, 5)
# print(r)

def print_argument(*args):
    for i in args:
        print(i,end=" ")


print_argument(1)
print_argument(1, 2)
print_argument(1, 2, 3)
print_argument(1, 2, 3, 4)
