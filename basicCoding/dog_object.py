class Dog():
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    def sit(self):
        print(self.breed.title() + " had sit")

    def jump(self):
        print(self.breed.title() + " was jump!")

my_dog = Dog('hasky', 4)
moms_dog = Dog('koly', 7)

print("This is " + my_dog.breed + " and it's a " + str(my_dog.age) + " years old ")
my_dog.jump()
moms_dog.sit()
