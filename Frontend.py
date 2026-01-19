from tkinter import *
import Backend
POS = Tk()
POS.geometry("800x1000")
loginframe = Frame(POS)
salesframe = Frame(POS)
adminframe = Frame(POS)
auditframe = Frame(POS)


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
item_list = Listbox(salesframe, width=40)
item_list.grid(row=2,column=3,columnspan=3,rowspan=7,sticky='nsew')

def addtocart(event=None):
    Backend.buy(product_entry.get())
    item_list.insert(END,)







































logout_button = Button(salesframe,text="Log Out")
logout_button.grid(row=1,column=0,sticky="nsew",columnspan=2)
add_product_button = Button(salesframe,text="Add PRoduct")
add_product_button.grid(row=2,column=0,sticky="nsew")
remove_product_button = Button(salesframe,text="Remove PRoduct")
remove_product_button.grid(row=3,column=0,sticky="nsew")
change_stock_button = Button(salesframe,text="Change Stock")
change_stock_button.grid(row=4,column=0,sticky='nsew')
print_reciept_button = Button(salesframe,text="Print reciept")
print_reciept_button.grid(row=5,column=0,sticky='nsew')
sale_summary_button = Button(salesframe,text="Sales Summary")
sale_summary_button.grid(row=2,column=1,sticky='nsew')
add_user_button = Button(salesframe,text="Add User")
add_user_button.grid(row=3,column=1,sticky='nsew')
remove_user_button = Button(salesframe,text="Remove User")
remove_user_button.grid(row=4,column=1,sticky='nsew')
finish_transac_button = Button(salesframe,text="Finish Transaction")
finish_transac_button.grid(row=5,column=1,sticky="nsew")









POS.mainloop()