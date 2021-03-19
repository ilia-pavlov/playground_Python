numbers = [3, 51, 2, 8, 9, 10]
numbers.sort()
print(numbers)


numbers = [3, 51, 2, 8, 9, 10]
numbers.sort(reverse=True)
print(numbers)


numbers = [3, 51, 2, 8, 9, 10]
print(sorted(numbers))
print(numbers)


numbers = [3, 51, 2, 8, 9, 10]
print(sorted(numbers, reverse=True))
print(numbers)


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)