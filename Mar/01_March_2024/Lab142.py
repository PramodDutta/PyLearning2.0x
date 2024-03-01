try:
    with open("TestData.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as fnfr:
    print(fnfr)
finally:
    file.close()
    
    