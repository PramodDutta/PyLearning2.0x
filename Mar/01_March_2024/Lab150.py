try:
    a = 10/0
except Exception as e:
    print(e)
finally:
    print("This code should be executed")