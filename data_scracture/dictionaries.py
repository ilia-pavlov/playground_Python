# point = {"x": 1, "y": 2}
points = dict(x=1, y=2)
print(points["x"])

points["x"] = 10
print(points)

points["z"] = 20
print(points)

if "a" in points:
    print(points["a"])
# OR
print(points.get("a"))  # if you don't have value with key "a" return none
print(points.get("a", 0))  # if you don't have value with key "a" return 0

del points["x"]
print(points)

for key in points:
    print(key, points[key])

for key, value in points.items():
    print(key, value)

