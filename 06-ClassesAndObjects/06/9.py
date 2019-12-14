class University:
    def __init__(self):
        self.name = "Uek"
        self.fullname = "Uniwerystet Ekonomiczny w Krakowie"
        
    def new_name(self, name):
        self.name = name
        
    def new_fullname(self, fullname):
        self.fullname = fullname
    
    def print_fullname(self):
        print(self.fullname)
        
    def print_name(self):
        print(self.name)
        

u1 = University()
u1.print_name()
u1.new_fullname("qwer")
u1.print_fullname()

        
    