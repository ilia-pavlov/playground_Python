numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]


numbers = [1, 2, 3]
first, second, third = numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
first, second, *other = numbers
print(first)
print(other)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
first, *other, last = numbers
print(first, last)
print(other)