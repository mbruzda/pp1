x = [7, 5, 3, 5, 2, 7, 4]

def fun(x):
    tab=[]
    for i in x:
        pow = 0
        for j in x:
            if i == j:
                pow+=1
        if pow == 1:
            tab.append(i)
    return tab

tab = fun(x)