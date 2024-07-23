# python program to  convert degrees celcius to fahrenheit and celcius to fahrenheit
class Temperature:
    def __init__(self,fahrenheit, celcius):
        self.fahrenheit = fahrenheit
        self.celcius = celcius
        
        # converting celcius to fahrenheit
    def c(self):
        celcius = (self.fahrenheit - 32) *5/9
        return celcius
        
        # convrting fahrenheitto celcius
    def fah(self):
        fahrenheit=(self.celcius + 32) *5/9
        return fahrenheit
        
temp = Temperature(55, 45)
print(temp.c())
print(temp.fah())
