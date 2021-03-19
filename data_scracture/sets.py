# collection with no duplicates

numbers = [1, 2, 3, 3, 3, 4, 4]
first = set(numbers)
second = {1, 4, 5}

print(first | second)   # mixing collections and show only uniq characters
print(first & second)   # show with item is duplicate from both collections
print(first - second)
print(first ^ second)

if 1 in first:
    print("yes")