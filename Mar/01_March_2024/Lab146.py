with open("td.txt","r") as file:
    lines = file.readlines()
    
# print(lines)
for line in lines:
    print(line, end="")
    

with open('td.txt', 'a') as file:
    file.write("\nShreeram")
