
from openpyxl import load_workbook
file=load_workbook("DatabaseCap.xlsx")
file2 = file.active


def add_new():
    file2.append([input("enter product name: "),int(input("enter stocks: "))])
    


def change_stock():
    product_name = input("enter product name: ").title()
    quantity = int(input("enter new quantity: "))
    for rows in file2.iter_rows(min_row=2,values_only=True):
        if row[0] == product_name:
            rows[1]= quantity
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

def remv_item():
    item = input("Enter Item Id to remove: ").title()
    for row in file2.iter_rows(min_row=2,values_only=True):
        if row[0] == item:
            decision = input(f"are you sure you want to remove {row[0]}?(y/n): ").lower()
            if decision == "y":
                row[0]= None
                row[1]=None
                break
            else:
                remv_item() 
            d = input("item id not found, wanna try again? y/n: ").lower()
            if d == "y":
                remv_item()

for row in file2.iter_rows(min_row=2):
    print(row[0].value,row[1].value)
change_stock()
