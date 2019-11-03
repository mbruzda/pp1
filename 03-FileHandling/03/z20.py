tablica = []
f = open("evennumbers.txt", "w")
with open('../numbers.txt','r') as file:
    for i in file:
        if int(i)%2==0:
            f.write(i)
f.close
file.close
