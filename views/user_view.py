from tkinter import *
from tkinter import ttk
from modul_ticket import *

#create window
user = Tk()

user.geometry("1500x900")
user.title('انتخاب شخصیت')
user.configure(bg = 'light blue')


#label
label_id = Label(user, text = 'ID', font = ('B Titr', 10), bg = 'light blue')
label_id.place(x = 20,y = 37)

label_name = Label(user, text = 'Name', font = ('B Titr', 10), bg = 'light blue')
label_name.place(x = 20, y = 77)

label_family = Label(user, text = 'Family', font = ('B Titr', 10), bg = 'light blue')
label_family.place(x = 20, y = 117)

label_birthday = Label(user, text = 'Birthday', font = ('B Titr', 10), bg = 'light blue')
label_birthday.place(x = 20, y = 157)

label_username = Label(user, text = 'Username', font = ('B Titr', 10), bg = 'light blue')
label_username.place(x = 20, y = 197)

label_password = Label(user, text = 'Password', font = ('B Titr', 10), bg = 'light blue')
label_password.place(x = 20, y = 237)

label_lock = Label(user, text = 'Is_Locked', font = ('B Titr', 10), bg = 'light blue')
label_lock.place(x = 20, y = 320)

label_role1 = Label(user, text = 'Admin', font = ('B Titr', 10), bg = 'light blue')
label_role1.place(x = 20, y = 400)

label_role2 = Label(user, text = 'Custome', font = ('B Titr', 10), bg = 'light blue')
label_role2.place(x = 140, y = 400)

#Entry
entry_id = Entry(user, width = 30)
entry_id.place(x = 120, y = 42)

entry_name = Entry(user, width = 30)
entry_name.place(x = 120, y = 82)

entry_family = Entry(user, width = 30)
entry_family.place(x = 120, y = 122)

entry_birthday = Entry(user, width = 30)
entry_birthday.place(x = 120, y = 162)

entry_username = Entry(user, width = 30)
entry_username.place(x = 120, y = 202)

entry_password = Entry(user, width = 30)
entry_password.place(x = 120, y = 242)


#Checkbutton

checkbutton = Checkbutton(user, onvalue = True, offvalue = False, bg = 'light blue')
checkbutton.place(x = 110, y = 322)


#Radiobutton

choice = StringVar(value = " ")
radiobutton1 = Radiobutton(user, variable = choice, value = '1', bg = 'light blue')
radiobutton2 = Radiobutton(user, variable = choice, value = '2', bg = 'light blue')

radiobutton1.place(x = 80, y = 400)
radiobutton2.place(x = 220, y = 400)


#Buttons

btn_edit = Button(user, text = 'Edit', command = button_edit, width = 7, bg = 'dark gray')
btn_remove = Button(user, text = 'Remove', command = button_remove, width = 7, bg = 'dark gray')
btn_save = Button(user, text = 'Save', command = button_save, width = 20, bg = 'dark gray')

btn_edit.place(x = 50, y = 560)
btn_remove.place(x = 140, y = 560)
btn_save.place(x = 50, y = 620)


#Table

table = ttk.Treeview(user, columns = ('id', 'name', 'family', 'birthday', 'username', 'password', 'is_locked', 'role'), show = 'headings', height = 30)

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
user.mainloop()
