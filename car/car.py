class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def description_name(self):
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()

    def read_odometer(self):
        print("This car have pass " + str(self.odometer_reading) + " miles")

    def update_odometer(self, miles):
        if miles > self.odometer_reading:  # protect odometer from busters!!
            self.odometer_reading = miles
        else:
            print("Don't try it boy!")

    def increment_odometer(self, miles):
        if miles < 0:
            print("You baster!! You can not put NEGATIVE value! Don't even think about it =)")
        else:
            self.odometer_reading += miles






