tablica = []
with open('../numbers.txt','r') as file:
    for i in file:
        tablica.append(int(i))
file.close
tablica.sort()
for i in tablica:
    print(i, end=" ")