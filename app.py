for number in range(1, 101):
    if number % 2 and number % 3 == 0:
        print("Fizz and Buzz " + str(number))
    elif number % 2 == 0:
        print("buzz " + str(number))
    elif number % 3 == 0:
        print("fizz " + str(number))
    else:
        print(number)