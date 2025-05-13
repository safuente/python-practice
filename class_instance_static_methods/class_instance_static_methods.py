class Car:
    brand = "Generic"

    def __init__(self, model, year):
        self.model = model
        self.year = year

    # Instance method: uses 'self'
    def description(self):
        return f"This car is a {self.brand} {self.model} from {self.year}"

    # Class method: uses 'cls'
    @classmethod
    def set_brand(cls, new_brand):
        cls.brand = new_brand

    # Static method: uses neither 'self' nor 'cls'
    @staticmethod
    def is_vintage(year):
        return year < 1990


# ▶️ Using the methods

# Create an instance
car1 = Car("Civic", 1998)

# Call the instance method
print(car1.description())         # Output: This car is a Civic from 1998

# Call the class method changing brand for current and future instances
Car.set_brand("Honda")
print(Car.brand)                  # Output: Honda
print(car1.description())

# Call the static method
print(Car.is_vintage(1980))       # Output: True
print(Car.is_vintage(2005))       # Output: False

car2 = Car("Civic", 2005)
print(car2.description())


# Instance methods are used for most things. When you want to produce an action that uses the data stored in an object.
# Static methods are used to just place a method inside a class because you feel it belongs
# there (i.e. for code organisation, mostly!)
# Class methods are often used as factories.
