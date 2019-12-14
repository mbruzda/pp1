class Bank:
    def __init__(self,numer,saldo=None):
        self.no = numer
        if saldo:
            self.saldo = saldo
        else:
            self.saldo = 0
        
    def show_status(self):
        print("Rachunek nr: ", self.no)
        print("Saldo: ", '%.2f'%self.saldo, "\n")
        
    def withdraw(self, przelew):
        if przelew > self.saldo:
            print("Niewystarczajaca ilosc srodkow na koncie")
        else:
            self.saldo = self.saldo - przelew
            print("Wypłacono: ", przelew, "\n")
            
    def deposit(self, dep):
        self.saldo += dep
        print("Wplacono: ", dep)
        
            
                
b1 = Bank("12 3456 5555 9090 1111 0000 7722")
b1.show_status()
b1.deposit(23.30)
b1.show_status()
b1.withdraw(31.70)
b1.show_status()
b1.withdraw(14)
b1.show_status()
        
        
    
        
    
        