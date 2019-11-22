def podatek(n):
    if n<=5000:
        tax = n*0.17
        return(tax)
    else:
        return 850 + (n - 5000)*0.32

x=float(input("Dochod: "))
print(podatek(x))
