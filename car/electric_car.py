from car import Car


class Battery:
    def __init__(self, battery=100):
        self.battery = battery

    def description_battery(self):
        print("This car have a " + str(self.battery) + " KV battery power")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def description_name(self):
        desc = str(self.year) + ' ' + self.model
        return desc.title()