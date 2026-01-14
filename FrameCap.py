from openpyxl import load_workbook
wb =load_workbook("DatabaseCap.xlsx")
ws= wb.active


def add_new():
    ws.append([input("enter product name: "),int(input("enter stocks: "))])
    wb.save("DatabaseCap.xlsx")
    


def change_stock():
    product_name = input("enter product name: ")
    found=False
    for rows in ws.iter_rows(min_row=2):
        if rows[0].value == product_name:
            found=True
            rows[1].value = int(input("enter new quantity: "))
            wb.save("DatabaseCap.xlsx")
            print ("stock updated")
            
            break
    if not found:
        print(f"{product_name} not found")    

def remv_item():
    item = input("Enter Item ID to remove: ").title()
    found = False

    for row in ws.iter_rows(min_row=2):
        if row[0].value== item:
            found = True
            decision = input(
                f"Are you sure you want to remove {row[0].value}? (y/n): "
            ).lower()

            if decision == "y":
                row[0].value = None
                row[1].value = None
                wb.save("DatabaseCap.xlsx")
                print("Item removed successfully.")
            else:
                print("Removal cancelled.")
            break

    if not found:
        dec = input(f"{item} not found, press r to retry").lower()
        if dec == "r":
            remv_item()

for row,row1 in ws.iter_rows(min_row=2,values_only=1):
    if row==None:
        continue
    print(row,row1)


