class Animals:
    def eat(self):
        print("eat")


class Bird(Animals):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass  # the issues is chicken can't fly so avoid complexity of inheritance.
