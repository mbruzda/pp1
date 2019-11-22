def pow(x, n):
    if n==0:
        return 1;
    if n==1:
        return x;
    if n>1:
        return x * pow(x, n-1)
    
    
print(f'5 do potęgi 7 wynosi {pow(5,7)}')