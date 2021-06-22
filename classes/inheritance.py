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
m.eat()
print(f'Age is {m.age} and eyes color is {m.eyes_color}')