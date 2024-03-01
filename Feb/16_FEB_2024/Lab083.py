set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}
subset = set2.issubset(set1)
print(subset)

set1 = set(["TheTestingAcademy", "For", "TheTestingAcademy."])
print(set1)

for i in set1:
	print(i)
 
 
set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])

print(set1)
set1.remove(5)
set1.remove(6)
print(len(set1)) #
