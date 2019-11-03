import re
komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
suma=0
for i in cyfry:
    x=int(i)
    suma=suma+x
srednia=suma/len(cyfry)
print(f'Średnia temperatur wynosi {srednia}')