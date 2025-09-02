# #mylist = [1, 2, 3, 4, 5]
# # mytuple = (1, 2, 3, 4)
# # myset = {2, 3, 4}
# # mydict = {"name": "Odallo", "Age": 12}

# # print(mydict)

# nums = [x for x in range(10) if x%2 == 0]
# print(nums)

# word = "Hello"

# for letter in word:
#     print(letter)


# for index, letter in enumerate(word):
#     print(index, letter)


# def greet(name, *args, **kwargs):
#     print(f"Hello {name}")
#     print("Extra args:", args)
#     print("Keyword args:", kwargs)

# greet("Odallo", "Dev", "Student", role="Pythonista")


# try:

#     with open("file.txt", "w") as a:
#         a.write("A Python Refresher")
#     with open("file.txt", "r") as a:
#         print(a.read())
# except Exception as e:
#     print("e")

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        return f"This vehicle has {self.odometer_reading} miles on it."

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def fill_gas_tank(self):
        return "Gas tank is full."

# Test it
my_car = Car("Toyota", "Camry", 2020, "Gasoline")
print(my_car.get_descriptive_name())
print(my_car.read_odometer())
my_car.update_odometer(15000)
print(my_car.read_odometer())
print(my_car.fill_gas_tank())