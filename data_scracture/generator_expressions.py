values = [x * 2 for x in range(10)]  # values is a list
for x in values:
    print(x)

values = (x * 2 for x in range(10))  # values is a generator object
print(values)
for x in values:
    print(x)

print("------------------------------------------------------")

from sys import getsizeof

values = (x * 2 for x in range(1000))
print("gen:", getsizeof(values))

values = [x * 2 for x in range(1000)]
print("list:", getsizeof(values))