suma=0
with open('../Numbers.txt', 'r') as file:
    for line in file:
        x=int(line)
        suma+=x
        
print(suma)    
