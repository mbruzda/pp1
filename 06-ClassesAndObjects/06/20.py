class Plane:
    def __init__(self, aircraft, no, vel=None, alt=None):
        self.aircraft = aircraft
        self.flight_no = no
        self.destination = None
        self.velocity = vel
        self.altitude = alt
        
    def show_status(self):
        print(f"Tu {self.flight_no}, moja wysokosc lotu to {self.altitude}m\n")
    
    def start(self, alt):
        while(alt <= 1000 or alt >= 2000):
            alt = int(input("Podaj wysokosc z zakresu 1000 - 2000: "))
        else:
            self.altitude = alt
    def rise(self,m=0):
        if self.altitude + m > 11000:
            self.altitude = 11000
            print("Alert wysokosci! Wysokosc zbyt wysoka.")
        else:
            self.altitude += m
            
    def fall(self,m=0):
        if self.altitude - m < 300:
            self.altitude = 300
            print("Alert wysokosci! Wysokosc zbyt niska. Wysokosc = 300m\n")
        else:
            self.altitude -= m
            
    def land(self):
        if self.altitude <= 300:
            self.altitude = 0
            print("Wylądowano pomyslnie")
        else:
            print("Zbyt duza wysokosc")
            
    def setaltitude(self, alt):
        if alt>300 and alt<11000:
            self.altitude = alt
            print(f"Zmieniono wysokosc na {alt}m\n")
        else:
            print("Nieprawidlowa wysokosc")
        

p1 = Plane("AIRPLANE", "LOT881")
p1.start(1000)
p1.show_status()
p1.setaltitude(8900)
p1.show_status()
p1.fall(8700)
p1.show_status()
p1.land()
            
            
        
        
    