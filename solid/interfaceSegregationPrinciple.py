from abc import ABC, abstractmethod

# Interface Animal para definir os métodos que um animal deve implementar
class Animal(ABC):
    @abstractmethod
    def eat():
        pass
    @abstractmethod
    def sleep():
        pass

# Interface ave para definir os métodos que uma ave deve implementar
class Bird(ABC):
    @abstractmethod
    def fly():
        pass

# Classe Pato que implementa ambas as interfaces
class Duck(Animal, Bird):
    def eat(self):
        print("Duck eating")
    
    def sleep(self):
        print("Duck sleeping")

    def fly(self):
        print("Duck flying")

# Classe Cachorro que implementa apenas a interface Animal, pois um cachorro não necessita dos métodos da interface Ave, 
# assim cumprindo o princípio da segregação de interface, pois o mesmo não necessita implementar um método que não vai utilizar
class Dog(Animal):
    def eat(self):
        print("Dog eating")

    def sleep(self):
        print("Dog sleeping")

if __name__ == '__main__':
    dog = Dog()
    duck = Duck()
    dog.eat()
    duck.fly()