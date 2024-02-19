browser = str(input("Enter the browser name:\n"))
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome code executed!")
    case "firefox":
        print("Firefox code executed!")
    case "google":
        print("Google browser executed!")
    case browser if browser == "fb":
        print("you are enter facebook")
    case browser if browser == "insta":
        print("you are enter instagram")
    case _:
        print("No browser Found!")
