import math

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display(self):
        print(f"Vehicle: {self.make} {self.model}")
    
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def display(self):
        print(f"Car: {self.make} {self.model}, Fuel Type: {self.fuel_type}")

    def fuel_efficiency(self, mileage=None):
        if mileage is None:
            print("Fuel efficiency data not provided.")
        else:
            print(f"Car mileage: {mileage} km/l")
        
class Truck(Vehicle):
    def __init__(self, make, model, load_capacity):
        super().__init__(make, model)
        self.load_capacity = load_capacity
    
    def display(self):
        print(f"Truck: {self.make} {self.model}, Load Capacity: {self.load_capacity} tons")

    def fuel_efficiency(self, load=None):
        if load is None:
            print("Fuel efficiency data not provided.")
        else:
            print(f"Truck fuel efficiency for load {load} tons: 8 km/l")

vehicle = Vehicle("Generic", "Model X")
car = Car("Toyota", "Corolla", "Petrol")
truck = Truck("Volvo", "FH", 10)

vehicle.display()
car.display()
truck.display()

car.fuel_efficiency()
car.fuel_efficiency(15)

truck.fuel_efficiency()
truck.fuel_efficiency(5)