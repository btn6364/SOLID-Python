from abc import ABC, abstractmethod

class Shape(ABC): 
    
    @abstractmethod
    def calculate_area(self): 
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

def get_total_area(shapes):
    return sum(shape.calculate_area() for shape in shapes)

print(f"Total area = {get_total_area([Rectangle(10, 5), Square(5)])}")