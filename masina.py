class Car:
    def __init__(self, brend:str, fuel:float, consumption:float):
        self.brend = brend
        self.fuel = fuel 
        self.consumption = consumption  
        
    def __str__(self):
        return f'{self.brend} cu consum de {self.consumption} si are {self.fuel:.2f} litri de motorina'
        
    def drive(self,km) :
        litri = (km / 100) *  self.consumption
        if litri <= self.fuel :
            self.fuel -= litri 
            
    
    def refuel(self, liters) :
        self.fuel += liters
        
    def can_drive(self, km) :
          litri = (km / 100) *  self.consumption
          return litri <= self.fuel
          
    def get_fuel(self):
        return self.fuel 
        
        
