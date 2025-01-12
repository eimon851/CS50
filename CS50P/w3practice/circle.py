import math

class Circle:
    # initialize the circle object with a given radius
    def __init__(self, radius):
        self.radius = radius

    # self kw is used to refer to instance of class
    # automatically passed as first arg of any method
    def calculate_area(self):
        area = math.pi * self.radius**2
        return area

    def calculate_perimeter(self):
        perimeter = 2*math.pi*self.radius
        return perimeter

radius = int(input("Radius: "))
circle = Circle(radius)
print(circle.calculate_area())
print(circle.calculate_perimeter())
