from tkinter import *
from tkinter import ttk
from modul_ticket import *

#create window
ticket = Tk()

ticket.geometry("1500x900")
ticket.title('بیلط هواپیما')
ticket.configure(bg = 'gray')


#lable
lable_id = Label(ticket, text = 'ID', font = ('B Titr', 10), bg = 'gray')
lable_id.place(x = 20,y = 37)

lable_name = Label(ticket, text = 'Name', font = ('B Titr', 10), bg = 'gray')
lable_name.place(x = 20, y = 77)

lable_family = Label(ticket, text = 'Family', font = ('B Titr', 10), bg = 'gray')
lable_family.place(x = 20, y = 117)

lable_birthday = Label(ticket, text = 'Birthday', font = ('B Titr', 10), bg = 'gray')
lable_birthday.place(x = 20, y = 157)

lable_username = Label(ticket, text = 'Username', font = ('B Titr', 10), bg = 'gray')
lable_username.place(x = 20, y = 197)

lable_password = Label(ticket, text = 'Password', font = ('B Titr', 10), bg = 'gray')
lable_password.place(x = 20, y = 237)

lable_lock = Label(ticket, text = 'Is_Locked', font = ('B Titr', 10), bg = 'gray')
lable_lock.place(x = 20, y = 320)

lable_role1 = Label(ticket, text = 'Admin', font = ('B Titr', 10), bg = 'gray')
lable_role1.place(x = 20, y = 400)

lable_role2 = Label(ticket, text = 'Custome', font = ('B Titr', 10), bg = 'gray')
lable_role2.place(x = 140, y = 400)

#Entry
entry_id = Entry(ticket, width = 30)
entry_id.place(x = 120, y = 42)

entry_name = Entry(ticket, width = 30)
entry_name.place(x = 120, y = 82)

entry_family = Entry(ticket, width = 30)
entry_family.place(x = 120, y = 122)

entry_birthday = Entry(ticket, width = 30)
entry_birthday.place(x = 120, y = 162)

entry_username = Entry(ticket, width = 30)
entry_username.place(x = 120, y = 202)

entry_password = Entry(ticket, width = 30)
entry_password.place(x = 120, y = 242)


#Checkbutton

checkbutton = Checkbutton(ticket, onvalue = True, offvalue = False, bg = 'gray')
checkbutton.place(x = 110, y = 322)


#Radiobutton

choice = StringVar(value = " ")
radiobutton1 = Radiobutton(ticket, variable = choice, value = '1', bg = 'gray')
radiobutton2 = Radiobutton(ticket, variable = choice, value = '2', bg = 'gray')

radiobutton1.place(x = 80, y = 400)
radiobutton2.place(x = 220, y = 400)


#Buttons

btn_edit = Button(ticket, text = 'Edit', command = button_edit, width = 7, bg = 'dark gray')
btn_remove = Button(ticket, text = 'Remove', command = button_remove, width = 7, bg = 'dark gray')
btn_save = Button(ticket, text = 'Save', command = button_save, width = 20, bg = 'dark gray')

btn_edit.place(x = 50, y = 560)
btn_remove.place(x = 140, y = 560)
btn_save.place(x = 50, y = 620)


#Table

table = ttk.Treeview(ticket, columns = ('id', 'name', 'family', 'birthday', 'username', 'password', 'is_locked', 'role'), show = 'headings', height = 30)

table.heading('id', text = 'ID')
table.heading('name', text = 'Name')
table.heading('family', text = 'Family')
table.heading('birthday', text = 'Birthday')
table.heading('username', text = 'Username')
table.heading('password', text = 'Password')
table.heading('is_locked', text = 'Is Locked')
table.heading('role', text = 'Role')

table.column('id', width = 60)
table.column('name', width = 140)
table.column('family', width = 140)
table.column('birthday', width = 80)
table.column('username', width = 140)
table.column('password', width = 140)
table.column('is_locked', width = 80)
table.column('role', width = 80)


table.place(x = 500, y = 40)
ticket.mainloop()
