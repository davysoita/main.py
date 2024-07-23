# python program to find area and perimeter of a circle
import math
class circle:
    def __init__(self, radius, diameter, pi):
        self.radius = radius
        self.diameter = diameter
        self.pi = pi
    def area(self):
        a = pow(self.radius, 2)
        output = self.pi*a 
        return output
    def perimeter(self):
        solution = 2*self.pi*self.diameter
        return solution
cir=circle(56,22,3.14)
print(cir.area())
print(cir.perimeter())
     
    