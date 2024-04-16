from abc import ABC, abstractmethod

# Stable interface definition
# Definição da interface estável
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

# Implementation of the first variation of the service
# Implementação da primeira variação do serviço
class Car(Vehicle):
    def __init__(self, color):
        self.color = color
        self.wheels = 4

    def drive(self):
        print("Driving car")

# Implementation of the second variation of the service
# Implementação da segunda variação do serviço
class Motorcycle(Vehicle):
    def __init__(self, color):
        self.color = color
        self.wheels = 2

    def drive(self):
        print("Driving motorcycle")

# Cliente interagindo com a interface estável
class Driver:
    def __init__(self, name, vehicle: Vehicle, age):
        self.name = name
        self.vehicle = vehicle
        self.age = age
    
    def driveVehicle(self):
        self.vehicle.drive()

# Exemplo de uso
if __name__ == "__main__":
    vehicle_a = Car("red")
    vehicle_b = Motorcycle("yellow")

    driver_a = Driver("Vitor", vehicle_a, 21)
    driver_a.driveVehicle()  # Output: Driving car

    driver_b = Driver("Lucas", vehicle_b, 22)
    driver_b.driveVehicle()  # Output: Driving motorcycle
