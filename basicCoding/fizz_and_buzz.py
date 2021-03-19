def fizz_buzz(number):
    if number % 2 == 0 and number % 3 == 0:
        print("FizzBuzz " + str(number))
    elif number % 2 == 0:
        print("buzz " + str(number))
    elif number % 3 == 0:
        print("fizz " + str(number))
    else:
        print(number)


fizz_buzz(int(input("choose the number :  ")))
