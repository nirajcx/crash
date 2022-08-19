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

    @staticmethod
    def prir(string):
        print('Hello tAES' + string)


class Battery():
    def __init__(self, battery_capacity=85):
        self.battery_capacity = battery_capacity

    def battery_des(self):
        print('The battery capacity is ' + str(self.battery_capacity))

    def battery_range(self):
        if self.battery_capacity == 70:
            range = 240
        elif self.battery_capacity == 85:
            range = 300
        mess = "This car can go approximately " + \
            str(range) + " miles on full charge"
        print(mess)


class ElectricCar(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        self.battery = Battery()

    def prinelec(self):
        return f"The brand is {self.brand} model is {self.model} and year is {self.year}"

    def fill_gas(self):
        print('Electric cars doest require gas to run')