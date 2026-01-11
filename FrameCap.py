
from openpyxl import load_workbook
file=load_workbook("DatabaseCap.xlsx")
file2 = file.active

file2.append([input("enter product name: "),int(input("enter stocks"))])
    
file.save("DatabaseCap.xlsx")
for f,q in file2.iter_rows(min_row=2,values_only=1):
    print(f,q)