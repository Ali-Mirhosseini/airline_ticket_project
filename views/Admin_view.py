from tkinter import *
from tkinter import ttk
from modul_ticket import *

#Create window

auto_save = Tk()

auto_save.geometry('1500x900')
auto_save.title('ذخیره خودکار بلیط')
auto_save.configure(bg = 'light blue')

#Label

label_airline_auto = Label(auto_save, text = 'Airline', font = ('B titr', 10), bg = 'light blue')
label_airline_auto.place(x = 20 , y = 37)

label_source_auto = Label(auto_save, text = 'Source', font = ('B Titr', 10), bg = 'light blue')
label_source_auto.place(x = 20, y = 77)

label_destination_auto = Label(auto_save, text = 'Destination', font = ('B Titr', 10), bg = 'light blue')
label_destination_auto.place(x = 20, y = 117)

label_start_date_time_auto = Label(auto_save, text = 'Start date time', font = ('B Titr', 10), bg = 'light blue')
label_start_date_time_auto.place(x = 20, y = 157)

label_end_date_time_auto = Label(auto_save, text = 'End date time', font = ('B Titr', 10), bg = 'light blue')
label_end_date_time_auto.place(x = 20, y = 197)

label_price_auto = Label(auto_save, text = 'Price', font = ('B Titr', 10), bg = 'light blue')
label_price_auto.place(x = 20, y = 237)

#Entry

entry_airline_auto = Entry(auto_save, width = 30)
entry_airline_auto.place(x = 160, y = 42)

entry_source_auto = Entry(auto_save, width = 30)
entry_source_auto.place(x = 160, y = 82)

entry_destination_auto = Entry(auto_save, width = 30)
entry_destination_auto.place(x = 160, y = 122)

entry_start_date_time_auto = Entry(auto_save, width = 30)
entry_start_date_time_auto.place(x = 160, y = 162)

entry_end_date_time_auto = Entry(auto_save, width = 30)
entry_end_date_time_auto.place(x = 160, y = 202)

entry_price_auto = Entry(auto_save, width = 30)
entry_price_auto.place(x = 160, y = 242)

#Button

btn_edit = Button(auto_save, text = 'Edit', command = button_edit, width = 7, bg = 'dark gray')
btn_remove = Button(auto_save, text = 'Remove', command = button_remove, width = 7, bg = 'dark gray')
btn_save = Button(auto_save, text = 'Save', command = button_save, width = 20, bg = 'dark gray')

btn_edit.place(x = 70, y = 400)
btn_remove.place(x = 160, y = 400)
btn_save.place(x = 70, y = 460)

#Table

table = ttk.Treeview(auto_save, columns = ('capacity'), show = 'headings', height = 30)

table.heading('capacity', text = 'Capacity')

table.column('capacity', width = 400)

label_capacity = Label(auto_save, text = 'Capacity', font = ('B titr', 10), bg = 'white')
label_capacity.place(x = 600 , y = 310)

entry_start_capacity = Entry(auto_save, width = 10, bg = 'light gray')
entry_start_capacity.place(x = 730, y = 315)


table.place(x = 500, y = 250, height = 150)

auto_save.mainloop()