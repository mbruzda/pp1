def check(n,x,y):
    if n>x and n<y:
        return True
    else:
        return False
    
n = int(input("Podaj liczbe n: "))
x, y = input("Podaj zakres (dwie wartosci oddzielone spacja): ").split()

if check(n, int(x), int(y)):
    print("Zawiera sie")
else:
    print("Nie zawiera sie")
    