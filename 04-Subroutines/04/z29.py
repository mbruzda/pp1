lang = ['Java', 'Python', 'JavaScript', 'C++', 'Ruby', 'Perl', 'PHP', 'C', 'Android']
demand = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]

def rysujwykres(jezyki, wartosci):
    for i in range(len(jezyki)-1):
        print(lang[i], *'#'*wartosci[i],"\n")
        
rysujwykres(lang, demand)

        

    