from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = 3.14
        return pi * self.radius ** 2

rectangle = Rectangle(5, 10)
circle = Circle(5)
print(rectangle.area())
print(circle.area())