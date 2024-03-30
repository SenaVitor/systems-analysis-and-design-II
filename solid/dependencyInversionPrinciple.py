from abc import ABC, abstractmethod

# Interface de carro que possui os métodos que um carro deve implementar
class EngineInterface(ABC):
    @abstractmethod
    def speedUp(self):
        pass

# Classe Motor que implementa a interface
class Engine(EngineInterface):
    # Método da interface que aumenta a velocidade
    def speedUp(self, car):
        car.speed += 10
        print(f'Speed = {car.speed}')


# Classe Carro
class Car():
    # Método construtor
    def __init__(self, model, color, engine: EngineInterface):
        self.model = model
        self.color = color
        self.engine = engine
        self.speed = 0

    # Método para dirigir o carro que depende apenas de uma abstração de motor (engine)
    def drive(self):
        car = self
        self.engine.speedUp(car)

    # Método para exibir as informações do carro
    def showInfos(self):
        print(f'Model: {self.model} \nColor: {self.color}')

if __name__ == '__main__':
    engine = Engine()
    car = Car("Gol", "Red", engine)
    car.showInfos()
    car.drive()
    car.drive()