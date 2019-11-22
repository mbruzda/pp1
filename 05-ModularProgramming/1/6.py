import csv
lp=0
with open('../employees.csv', newline='') as f:
    reader = csv.reader(f)
    print(reader)
#    for row in reader:
#        if(lp==0):
#            print(f"#     {row[1]}    {row[2]}    {row[3]}")
#            print("="*50)
#            lp+=1
#        else:    
#            print(f"{lp}     {row[1]}    {row[2]}    {row[3]}")
#            lp+=1