from random import randint

def rand():
    return(randint(0,50))

even=0
for i in range(1000):
    if (rand()%2==0):
        even += 1
        
print(f"Liczby Parzyste: {even/10}%\nLiczby nieparzyste: {(1000-even)/10}%")        
    
