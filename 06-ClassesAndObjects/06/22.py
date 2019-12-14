import random

class Doctor:
    def __init__(self, temp=None):
        self.temp = temp
    
    def random(self):
        self.temp = round(random.uniform(34,42.1), 1)
        
    def show_status(self):
        print(self.temp)
        

p1 = Doctor()
p1.random()
p1.show_status()
        
        
    