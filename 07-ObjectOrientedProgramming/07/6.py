class Film:
    cinema = "Multikino, Kraków"
    
    def __init__(self, title):
        self.title = title
        
    def __str__(self):
        return f"{self.title} ({Film.cinema})"
    
f1 = Film('Pat i Kot')
print(f1)