class Animals:
    def __init__(self):
        self.age = 1


    def eat(self):
        print("eat")


class Mammal(Animals):
    def __init__(self):  # we overriding constructor, so fist constructor with age we NOT execute
        super().__init__()   # after adding super class we got access to first constructor
        self.weight = 2
        # super().__init__() Now Mammal constructor will executed first ans then Animal
    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)
