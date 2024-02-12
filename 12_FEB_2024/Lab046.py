# Triangle Cla
# side1 == side2 == side 3 ->  Eq.
# side 1 == side 2 or side 2 == side 3 or side 1 == side 3 -> ISO
# else -> Scalene

side1 = float(input("Enter the side 1\n"))
side2 = float(input("Enter the side 2\n"))
side3 = float(input("Enter the side 3\n"))

if side1 == side2 == side3:
    print("EQ")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("ISO")
else:
    print("Scalene")
