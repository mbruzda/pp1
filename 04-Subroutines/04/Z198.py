def suma(x):
    if x == 1:
       return 1
    if x>1:
        return x + suma(x-1)

print(suma(int(input("Podaj n: "))))
