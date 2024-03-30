from abc import ABC, abstractmethod

# Classe abstrata para as formas geométricas
class Shape():
    # Método abstrato que as classes filhas deverão implementar
    def getArea(self, shape):
        pass

# Classe Quadrado que herda da classe Shape
class Square(Shape):
    # Método construtor
    def __init__(self, size):
        self.size = size

    # Método da classe abstrata
    def getArea(self, shape):
        area = self.size ** 2
        print(f'Square area = {area}')

# Classe Retângulo que herda da classe Shape
class Rectangle(Shape):
    # Método construtor
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    # Método da classe abstrata
    def getArea(self, shape):
        area = self.height * self.width
        print(f'Rectangle area = {area}')

if __name__ == '__main__':
    shape1 = Square(2)
    shape2 = Rectangle(2, 8)
    # Como requisitado no princípio da substituição de Liskov, ambos os objetos podem substituir o objeto pai (Shape)
    shape1.getArea(shape1)
    shape2.getArea(shape2)