values = []
for x in range(5):
    values.append(x * 2)
print(values)

# [expression for item in items]
values = [x * 2 for x in range(5)]
print(values)

values = {x * 2 for x in range(5)}
print(values)

values = {}
for x in range(5):
    values[x] = x * 2
print(values)
# OR
values = {x: x * 2 for x in range(5)}
print(values)