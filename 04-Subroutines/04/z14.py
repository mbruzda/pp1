def wystepuje(x, tab):
    wys=False
    for i in tab:
        if x==i:
            wys=True
        else:
            continue
    return(wys)

x=23
tablica=[15, 38, 7, 23, 14]

print(f"Liczba: {x}\nTablica: {tablica}")
if wystepuje(x, tablica):
    print("Wystepuje")
else:
    print("Nie wystepuje")

