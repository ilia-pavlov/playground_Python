class Point:
    default_color = "red"  # hard coding class level attribute

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "yellow"  # change hard coding attribute in class

point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
#  point.z = 10
point.draw()

another = Point(3, 4)
print(another.default_color)
another.draw()
