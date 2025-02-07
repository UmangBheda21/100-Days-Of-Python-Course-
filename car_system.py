# Task 1: Create Car class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

# Create an object and call car_info()
car1 = Car("Toyota", "Corolla", 2022)
car1.car_info()  # Output: Car: Toyota Corolla, Year: 2022

# Task 2: Create ElectricCar class using inheritance
class ElectricCar(Car):  
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)  # Call parent constructor
        self.battery_capacity = battery_capacity  # New attribute for ElectricCar

    def battery_info(self):
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Create ElectricCar object
e_car = ElectricCar("Tesla", "Model S", 2023, 100)
e_car.car_info()  # Output: Car: Tesla Model S, Year: 2023
e_car.battery_info()  # Output: Battery Capacity: 100 kWh

# Task 3: Override car_info() to include battery info
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def car_info(self):  # Overriding parent method
        print(f"Electric Car: {self.brand} {self.model}, Year: {self.year}, Battery: {self.battery_capacity} kWh")

# Create an object and call overridden method
e_car2 = ElectricCar("Tesla", "Model X", 2024, 120)
e_car2.car_info()  # Output includes battery info
