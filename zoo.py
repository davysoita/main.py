# python project to manage a zoo
class Animal:
    def make__sound(self, name,species):
        self.name = name
        self.species = species
        
class Mammal(Animal):
    def num_legs(self, name, species, num_legs):
        Animal.__init__(name, species)
        self.num_legs = num_legs
    print("The dog barks") 
    
class Bird(Animal):
    def can__fly(self, name,species, can_fly):
        Animal.__init__(name, species)
        self.can_fly = can_fly
    print("The bird chants")
B=Bird()
B.Bird()
B.Mammal()
B.Animal()
M=Mammal()
M.Bird()
M.Mammal()
M.Animal()