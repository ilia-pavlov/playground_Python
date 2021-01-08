numbers = [1, 2, 3, 4, 5]
#first, second, third = numbers
#print(numbers)

first, *other, last = numbers
print(*other)
print(last)