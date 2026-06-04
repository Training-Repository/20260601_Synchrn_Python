from random import randint

# carCount = 0

class Car:
    # Class variable
    total_cars = 0

    # def __new__(cls):
    #     pass

    def __init__(self, make, model, year, color):
        # Instance variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.serial = Car.genSerial()

        # Increment the total number of cars
        # globals()["carCount"] += 1
        Car.total_cars += 1


    def start(self):
        # Instance method
        print(f"{self.year} {self.make} {self.model} is starting.")

    def __str__(self):
        # Method overriding for string representation
        return f"{self.year} {self.color} {self.make} {self.model}"

    def __repr__(self):
        # Method overriding for data representation
        # return f"[{type(self)}, {id(self)}] - {self.year} {self.color} {self.make} {self.model}"
        # Car.__bases__
        # Car.__mro__

        # print(self.__class__)
        # print(self.__class__.__name__)
        return super().__repr__() + " --> " + f"[Count: {Car.total_cars}]  " + f"{self.make} {self.model} {self.serial}"
    
    @classmethod
    def car_count(cls):
        # Class method to access class variable
        return cls.total_cars

    @staticmethod
    def genSerial():
        return randint(1000, 9999)



# Create instances of the Car class
car1 = Car("Toyota", "Camry", 2022, "Blue")
car2 = Car("Honda", "Accord", 2022, "Red")

# Call instance methods
car1.start()
car2.start()

# print(car1.make, car1.model, car1.year, car1.color)
# print(car1)
# print(str(car1))
# print(car1.__str__())
# print(car1.__repr__())
print(repr(car1))
print(repr(car2))

# Access class method
print("Total Cars:", car1.car_count())

# LEGB - Local, External, Global , Builtins