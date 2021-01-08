number = 100
while number > 0:
    print(number)
    number //= 2

print(" ")

command = ""
while command.lower() !="quit":
    command = input(">")
    print("ECHO", command)
    print("for close program type \"quit\"")


while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break