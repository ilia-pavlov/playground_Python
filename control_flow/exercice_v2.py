count = 0
for x in range(1, 20):
    while x % 2 == 0:
        count +=1
        print(x)
        break
print(f"We have {count} even numbers")
