numbers = [1, 2, 3]
print(*numbers)

values = list(range(5))
print(values)

values = [*range(5)]
print(values)

first = {"x": 10}
second = {"x": 1, "y": 2}
combined = {**first, **second, "z": 3}
print(combined)