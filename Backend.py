from openpyxl import load_workbook, Workbook
import random
from datetime import datetime
Inventory_Database = "Database.xlsx"
Sales_Database = "sale.xlsx"
user_database = "user.xlsx"

wb1 = load_workbook(Inventory_Database)
ws1 = wb1.active
wb2 = load_workbook(Sales_Database)
ws2 = wb2.active
wb3 = load_workbook(user_database)
ws3 = wb3.active

sales_id = random.randint(10000, 99999)

def product_name(product_id):
    for row in ws1.iter_rows(min_row=1,values_only=True):
        if row[0] == product_id:
            return row[1]
    return None


def login(user,password):
    for row in ws3.iter_rows(min_row = 1,values_only = True):
        if row[0] == user and row[1] == password:
            return True
    return False    
def checkadmin(role):
    for row in ws3.iter_rows(min_row = 1,values_only = True):
        if row[1] == role:
            return True
    return False


def check_product(code):
    for cell in ws1.iter_rows(min_row=1, max_col=1, values_only=True):
        if cell[0] == code:
            return True
    return False

def get_price(code):
    for row in ws1.iter_rows(min_row=1, max_col=5, values_only=True):
        if row[0] == code:
            return row[3]

    return None
def print_reciept(sales_id):
    print("Reciept")
    print(f"Sales ID: {sales_id}")
    for row in ws2.iter_rows(min_row=1,values_only=True):
        if row[0] == sales_id:
            reciept = (row[2], row[3], row[4], row[5])
        return reciept

def update_stock(code, qty_sold):
    for row in ws1.iter_rows(min_row=2):
        if str(row[0].value).strip().upper() == code:
            current_stock = row[4].value
            new_stock = current_stock - qty_sold
            if new_stock < 0:
                print(f"Not enough stock for {code}! Only {current_stock} left.")
                return False
            row[4].value = new_stock
            return True
    return False 

def buy(product_id,qty):
    now = datetime.now()
    update_stock(product_id,qty)
    p = get_price(product_id)
    subtotal = float(p) * qty
    ws2.append([sales_id, now.strftime("%Y-%m-%d %H:%M:%S"), product_id, qty, p, float(subtotal)])
    
def save():
    wb2.save("sale.xlsx")
    wb1.save("Database.xlsx")
