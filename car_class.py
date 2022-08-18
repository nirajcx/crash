class Car():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        des = self.brand + ' '+self.model+' '+str(self.year)
        return des.title()

    def read_odometer(self):
        print('odometer reading is ' + str(self.odometer_reading))

    def update_odometer(self, mileage):
        """ Set the odometer reading to the given value. Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cant roll back the reading')


mycar = Car('BMW', 'M4 Sports', 2022)
print(mycar.get_descriptive_name())
mycar.odometer_reading = 23
mycar.read_odometer()
mycar.update_odometer(70)
mycar.read_odometer()
mycar.update_odometer(4)
mycar.read_odometer()
