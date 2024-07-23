# python program to find area and perimeter of a circle
import math
class circle:
    def __init__(self, r, d, pi):
        self.r = r
        self.d = d 
        self.pi = pi
    def area(self):
        a = pow(self.r, 2)
        output = self.pi*a 
        return output
    def perimeter(self):
        solution = 2*self.pi*self.d 
        return solution
cir=circle(7,14,3.14)
print(cir.area())
print(cir.perimeter())
     
    