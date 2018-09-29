class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set odometer to given value, if higher"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't move backwards")

    def increment_odometer(self, miles):
        """add miles to odometer"""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represents an electric car"""

    def __init__(self, make, model, year):
        """
        Initialize attr of parent class
        then attr specific to electric car
        """
        super().__init__(make, model, year)
        self.battery_size = Battery()

    def describe_battery(self):
        """print desc of battery"""
        print("this car has a " + str(self.battery_size) + "-kWh battery")

    def fill_gas_tank():
        """override non-existent method of parent class"""
        print("no can do")


class Battery():
    """simple model for Battery"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + "-kWh battery")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
