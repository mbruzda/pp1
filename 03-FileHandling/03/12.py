tablica = [32, 16,5,8,24,7]
with open('tablica.txt','a') as file:
    for i in tablica:
        file.write(str(i) + "\n")