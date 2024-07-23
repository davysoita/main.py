import math
class Circle:
    def __init__(self,r,d,pi):
        self.r = r
        self.d = d 
        self.pi =pi 
        
    def area(self):
        a=pow(self.r ,2)
        solution = self.pi*a 
        return solution
        
    def perimeter(self):
        result = 2*self.pi*self.d 
        return result
        
circle1=Circle(7,14,3.14)
print(circle1.area())
print(circle1.perimeter())
    
    