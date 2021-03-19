x = 10
y = 11

z = 0

z = x   # 10
x = y   # 11
y = z   # 10

print(x, y)

x = 10
y = 11


x, y = y, x
print("x", x)
print("y", y)