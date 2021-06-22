class Animals:
    def __init__(self):
        self.age = 1
        self.eyes_color = "hard code blue"

    def eat(self):
        print("eat")


class Mammal(Animals):
    def walk(self):
        print("walk")


class Fish(Animals):
    def swim(self):
        print("swim")


m = Mammal()
print(isinstance(m, Mammal))
print(issubclass(Mammal, Animals))