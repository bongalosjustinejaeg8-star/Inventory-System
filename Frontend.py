from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import Backend
import random
from openpyxl import load_workbook, Workbook
POS = Tk()
POS.geometry("800x1000")
loginframe = Frame(POS)
salesframe = Frame(POS)
adminframe = Frame(POS)
auditframe = Frame(POS)

Sales_ID = random.randint(1000,9999)
Temp_Total = 0.0
total_var = StringVar()
total_var.set("Total: ")
change = 0.0
is_admin = False
is_audit = False

#----------------------LOGIN FRAME-------------------------------------------------------------------
for i in range(11):
    loginframe.rowconfigure(i,weight=1)
for i in range(10):
    loginframe.columnconfigure(i,weight=2)
Label(loginframe,text="POSSYS SOLUTIONS",font=("times new roman",24,'bold')).grid(row=0,column=4,columnspan=3,sticky="nsew")
user_entry = Entry(loginframe)
Label(loginframe,text="USERNAME").grid(row=4,column=4)
user_entry.grid(row=4,column=5,sticky="ew")
Label(loginframe,text="Password").grid(row=5,column=4)
user_password = Entry(loginframe)
user_password.grid(row=5,column=5,sticky="ew")


def login_user():
    if Backend.login(user_entry.get(),user_password.get()):
        user_entry.delete(0,END)
        user_password.delete(0,END)
        loginframe.pack_forget()
        salesframe.pack(fill = "both",expand=True)
    else:
        warn = Label(loginframe,text = "Invalid Username or Password")
        warn.grid(row=9,column=5)

Button(loginframe, text = 'Login',command = login_user).grid(row=7,column=5,sticky="news")
loginframe.pack(fill = "both",expand=True)


#------------------------MAIN POS FRAME-----------------------------------------------------
for i in range(10):
    salesframe.rowconfigure(i,weight=1)
for i in range(7):
    salesframe.columnconfigure(i,weight=1)
Label(salesframe,text="POSSYS SOLUTIONS",font=('times new roman',24,'bold')).grid(row=0,column=3,columnspan=1,sticky='nswe')
product_entry = Entry(salesframe)
product_entry.grid(row=1,column=3,columnspan=3,sticky="we")
item_list = ttk.Treeview(salesframe,columns=("Product","Quantity","Price","Subtotal"),show="headings",height=10)
item_list.grid(row=2,column=3,columnspan=3,rowspan=7,sticky='nsew')

def addtocart(event=None):
    global Temp_Total
    product = product_entry.get()
    if "*" in product_entry.get():
        try:
            product_code, qty = product.split("*")
            product_code = product_code.strip()
            qty = int(qty.strip())
        except:
            messagebox.showerror("Invalid entry format!", "Use: Code * Quantity")
            product_entry.delete(0, END)
            return
    else:
        product_code = product
        qty = 1
    
    if Backend.check_product(product_code):
        Backend.buy(product_code,qty,Sales_ID)
        item_list.insert("",END,values=(Backend.product_name(product_code),qty,Backend.get_price(product_code),float(qty*Backend.get_price(product_code))))
        product_entry.delete(0, END)
        Temp_Total += float(qty*Backend.get_price(product_code))
        total_var.set(f"Total: {Temp_Total:.2f}")
    else:
        messagebox.showerror("WARNING","INVALID PRODUCT ID")
        product_entry.delete(0, END)
def finish_transaction():
    popup = Toplevel(POS)
    popup.title("Finish Transaction")
    popup.geometry("250x180")
    popup.grab_set()
    Label(popup,text = f"TOTAL: {Temp_Total}").pack()
    Label(popup,text="Cash Recieved:").pack()
    cash = Entry(popup)
    cash.pack()
    def changes(event=None):
        global change
        global Sales_ID
        try:
            change += (float(cash.get()) - Temp_Total)
            messagebox.showinfo("CHANGE",f" Your Change is: {change}")
            Sales_ID = random.randint(1000,9999)
            Backend.save()
            popup.destroy()


        except ValueError:
            messagebox.showerror("Invalid entry format!", "YOU CANNOT SUBTRACT THAT TO A NUMBER YEA?")
            cash.delete(0, END)

    Button(popup,text="Confirm",command=changes).pack()

def printreceipt():
    popup = Toplevel(POS)
    popup.title("PRINT RECEIPT")
    popup.geometry("700x500")
    popup.grab_set()
    Label(popup,text="Enter Trasaction ID").pack()
    transac_id = Entry(popup)
    transac_id.pack()
    item_list = ttk.Treeview(popup,columns=("Product","Quantity","Price","Subtotal"),show="headings",height=10)
    item_list.pack()
    def printrec():
        wb2 = load_workbook("sale.xlsx")
        ws2 = wb2.active
        for row in ws2.iter_rows(min_row=1,values_only=True):
            if row[0] == int(transac_id.get().strip()):
                item_list.insert("",END,values=(row[2], row[3], row[4], row[5]))
            
    def close():
        popup.destroy()
    Button(popup,text="Submit",command=printrec).pack()
    Button(popup,text="Close",command=close).pack()

def logout():
    pop = Toplevel(POS)
    pop.title("WARNING")
    pop.geometry("300x200")
    Label(pop,text="LOG OUT?",font=("times new roman",18,"bold")).pack()
    def yeah():
        pop.destroy()
        salesframe.pack_forget()
        loginframe.pack(fill = "both",expand=True)
    def nah():
        pop.destroy()
    Button(pop,text="Yes",command=yeah).pack()
    Button(pop,text="Nah",command=nah).pack()

def change_stock():
    Inventory_Database = "Database.xlsx"
    wb1 = load_workbook(Inventory_Database)
    ws1 = wb1.active
    popup = Toplevel(POS)
    popup.title("Change stock")
    popup.geometry("700x500")
    popup.grab_set()
    Label(popup,text="Enter Product ID").pack()
    product_entry = Entry(popup)
    product_entry.pack()
    Label(popup,text="Enter New Stock").pack()
    stock_entry = Entry(popup)
    stock_entry.pack()
    def confirmstock():
        if Backend.check_product(product_entry.get().strip().upper()):
            Backend.chnage_stock(product_entry.get().strip(),stock_entry.get().strip())
            messagebox.showinfo("STOCKS","Stocks has been updated")
            popup.destroy()
        else:
            messagebox.showwarning("WARNING","ID NOT FOUND")
    def close():
        popup.destroy()
    Button(popup,text="Submit",command=confirmstock).pack()
    Button(popup,text="Cancel",command=close).pack()




























product_entry.bind("<Return>",addtocart)
Label(salesframe,textvariable=total_var,font=("arial",18)).grid(column=4,row=9,sticky="nsew",pady=10)
logout_button = Button(salesframe,text="Log Out",command=logout)
logout_button.grid(row=1,column=0,sticky="nsew",columnspan=2)
add_product_button = Button(salesframe,text="Add PRoduct")
add_product_button.grid(row=2,column=0,sticky="nsew")
remove_product_button = Button(salesframe,text="Remove PRoduct")
remove_product_button.grid(row=3,column=0,sticky="nsew")
change_stock_button = Button(salesframe,text="Change Stock",command=change_stock)
change_stock_button.grid(row=4,column=0,sticky='nsew')
print_reciept_button = Button(salesframe,text="Print reciept",command=printreceipt)
print_reciept_button.grid(row=5,column=0,sticky='nsew')
sale_summary_button = Button(salesframe,text="Sales Summary")
sale_summary_button.grid(row=2,column=1,sticky='nsew')
add_user_button = Button(salesframe,text="Add User")
add_user_button.grid(row=3,column=1,sticky='nsew')
remove_user_button = Button(salesframe,text="Remove User")
remove_user_button.grid(row=4,column=1,sticky='nsew')
finish_transac_button = Button(salesframe,text="Finish Transaction",command=finish_transaction)
finish_transac_button.grid(row=5,column=1,sticky="nsew")








POS.mainloop()