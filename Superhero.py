# Parent superhero class
class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def introduce(self):
        return f"Hello,I am {self.name} and my  superpower is  {self.superpower}."
    
    def perform_action(self):
        return f"{self.name} is performing a heroic action!"
    # Child class (inheritace /polymorphism)
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, flight_speed):
        super().__init__(name, power)
        self.flight_speed = flight_speed

    def perform_action(self):
        return f"{self.name} is flying at a speed of {self.flight_speed} mph!"
    #Creating objects
    hero1 = Superhero("Captain Courage ", "Strength")
    hero2 = FlyingSuperhero("Sky Guardian", "Flight", 500)
# Using the objects
print(hero1.introduce())    
print(hero1.perform_action())
print(hero2.introduce())    
print(hero2.perform_action())
#End of class.py