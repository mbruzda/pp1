from random import randint

def rzut():
    x = randint(1, 7)
    return x

tab=[]

rzuty=int(input("Ile chcesz rzutów: "))
print("Wyrzucone oczka: ", end="")
for i in range(rzuty):
    tab.append(rzut())
    print(tab[i], end=" ")
print(f"\nSuma oczek: {sum(tab)}")