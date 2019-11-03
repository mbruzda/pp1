tablica = []
with open('../universities.txt','r') as file:
    for i in file:
        tablica.append(i)
file.close
tablica.sort()
with open('../universities.txt','w') as file:
    for i in tablica:
        file.write(i)
file.close        