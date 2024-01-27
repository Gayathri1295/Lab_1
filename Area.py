class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def get_area(self):
        return self.length * self.width
    
rect = Rectangle(3, 4)
print("Area of the rectangle :", rect.get_area())