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
    def drive(self):
        print("Driving car")

# Implementation of the second variation of the service
# Implementação da segunda variação do serviço
class Motorcycle(Vehicle):
    def drive(self):
        print("Driving motorcycle")

# Cliente interagindo com a interface estável
class Driver:
    def __init__(self, service: Vehicle):
        self.service = service
    
    def driveVehicle(self):
        self.service.drive()

# Exemplo de uso
if __name__ == "__main__":
    vehicle_a = Car()
    vehicle_b = Motorcycle()

    driver_a = Driver(vehicle_a)
    driver_a.driveVehicle()  # Output: Driving car

    driver_b = Driver(vehicle_b)
    driver_b.driveVehicle()  # Output: Driving motorcycle
