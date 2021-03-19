letters = ["a", "b", "c"]
for char in letters:
    print(char)


letters = ["a", "b", "c"]
for char in enumerate(letters):
    print(char)


letters = ["a", "b", "c"]
for index, char in enumerate(letters):
    print(index, char)