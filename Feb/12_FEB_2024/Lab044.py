# Break

#For -> 1 to 10 ->  range(1,11,1) , range(1,11)
# i = 5 -> break from the loop - kicked out from the loop.

for counter in range(0,100):
    print(counter)
    if counter == 5:
        break
print("Outside of the for loop")
