tablica = []
with open('../numbersinrows.txt','r') as file:
    for i in file:
        tablica.append(i.split(','))
        
print(tablica)