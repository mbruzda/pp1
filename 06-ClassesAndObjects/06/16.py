class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
        self.isopen = False
        self.currentpage = 0
        
    def open(self):
        self.isopen = True
    def close(self):
        self.isopen = False
        
    def nextpage(self):
        if self.isopen:
            self.currentpage += 1
        else:
            print("Ksiażka jest zamknieta")
            
    def prevpage(self):
        if self.isopen:
            self.currentpage -= 1
        else:
            print("Ksiażka jest zamknieta")
            
    def show_status(self):
        print(f'{self.name}\n{self.author}\npage {self.currentpage} of {self.pages}')
        
b1 = Book("Harry Potter", "JK Rowling", 350)
b1.open()
b1.show_status()
for i in range(33):
    b1.nextpage()
b1.show_status()
b1.close()
b1.nextpage()
            
        
        
    
        
    
        