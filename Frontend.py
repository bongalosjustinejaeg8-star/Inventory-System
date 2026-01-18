from tkinter import *
import Backend
POS = Tk()
POS.geometry("800x1000")
loginframe = Frame(POS).pack()
salesframe = Frame(POS)
adminframe = Frame(POS)
auditframe = Frame(POS)


#Login
user_entry = Entry()
user_entry.pack()
role = ['Admin','Cashier','Audit']
selected_role = StringVar()
selected_role.set(role[0])
options= OptionMenu(loginframe,selected_role, *role)
options.pack(pady=20)

def login_user():
    if Backend.login(user_entry.get(),selected_role.get()):
        if selected_role.get() == role[0]:
            loginframe.pack_forget()
            adminframe.pack()
        elif selected_role.get() == role[1]:
            loginframe.pack_forget()
            salesframe.pack()
        elif selected_role.get() == role[2]:
            loginframe.pack_forget()
            auditframe.pack()
    else:
        warn = Label(text = "Invalid")
        warn.pack()

Button(text = 'Login',command = login_user).pack()







POS.mainloop()