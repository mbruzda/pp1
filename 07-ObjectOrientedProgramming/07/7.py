class Student:
    uni = "UEK Krakow"
    album = 100000
    
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.album = Student.album
        Student.album+=1
    
    def __str__(self):
        return f'{self.name} ({self.album}), {self.major}, {Student.uni}'
    
    
s1 = Student("Marcin Bruzda", "Informatyka")
print(s1)
s2 = Student("Wiesław Wszywka" ,'Browarnictwo')
print(s2)