"""
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:    # "Age can not be a 0"
    print("You didn't enter a valid age.")
else:
    print("No exceptions where thrown")
"""

"""
try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions where thrown")
finally:  # always execute
    file.close()
"""
try:
    with open("app.py") as file:  # , open("another.txt") as targert:
        print("File opened.")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions where thrown")
