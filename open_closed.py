from math import pi
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape): 
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

class Circle(Shape): 
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius
    
    def calculate_area(self):
        return pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side ** 2

rectangle = Rectangle(width=10, height=5)
print(f"Rectangle Area = {rectangle.calculate_area()}")

circle = Circle(radius=5)
print(f"Circle area = {circle.calculate_area()}")

square = Square(side=5)
print(f"Square area = {square.calculate_area()}")