letters = ["a", "b", "c"]

# Add
letters.append("d")
letters.insert(0, "--")
print(letters)


# Remove
letters.pop()    # remove from letters end of the list
letters.remove("b")
print(letters)

del letters[0:2]
print(letters)

letters.clear()
print(letters)