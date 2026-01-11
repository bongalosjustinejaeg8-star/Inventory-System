
from openpyxl import load_workbook
file=load_workbook("DatabaseCap.xlsx")
file2 = file.active


def add_new():
    file2.append([input("enter product name: "),int(input("enter stocks: "))])
    
for f,q in file2.iter_rows(min_row=2,values_only=1):
    print(f,q)

def change_stock():
    c = input("enter product name: ").upper()
    d = int(input("enter new quantity: "))
    for rows in file2.iter_rows(min_row=2):
        item = rows[0]
        stock = rows[1]

        if item.value.upper() == c:
            stock.value = d
            file.save("DatabaseCap.xlsx")
            print ("stock updated")
            
            break
        else: 
            print("item not found")
            descicion = input("press any character to exit or A to add new product: ").upper()
            if descicion == "A":
                add_new()
            else:
                break

            
    