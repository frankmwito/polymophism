# polymorphic function
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * math.pow(self.radius, 2)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Square:
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return math.pow(self.side, 2)

def describe_shape():
    shape = input("Enter the shape (circle, rectangle, square): ").lower()
    if shape == "circle":
        radius = float(input("Enter the radius: "))
        circle = Circle(radius)
        print(f"The area of the circle is {circle.area():.2f}")
    elif shape == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        rectangle = Rectangle(length, width)
        print(f"The area of the circle is {rectangle.area():.2f}")
    elif shape == "square":
        side = float(input("Enter the side: "))
        square = Square(side)
        print(f"The area of the circle is {square.area():.2f}")
        
    else:
        print("Unknown shape")
        
describe_shape()