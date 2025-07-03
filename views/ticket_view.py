from tkinter import *
from modul_ticket import *
from tkinter import ttk

#Creat window
ticket = Tk()

ticket.geometry('1700x900')
ticket.title('بلیط هواپیما')
ticket.configure(bg = 'light blue')

#Label

label_id = Label(ticket, text = 'ID', font = ('B Titr', 10), bg = 'light blue')
label_id.place(x = 20,y = 37)

label_ticket_code = Label(ticket, text = 'Ticket code', font = ('B Titr', 10), bg = 'light blue')
label_ticket_code.place(x = 20, y = 77)

label_source = Label(ticket, text = 'Source', font = ('B Titr', 10), bg = 'light blue')
label_source.place(x = 20, y = 117)

label_destination = Label(ticket, text = 'Destination', font = ('B Titr', 10), bg = 'light blue')
label_destination.place(x = 20, y = 157)

label_airline = Label(ticket, text = 'Airline', font = ('B Titr', 10), bg = 'light blue')
label_airline.place(x = 20, y = 197)

label_start_date_time = Label(ticket, text = 'Start date time', font = ('B Titr', 10), bg = 'light blue')
label_start_date_time.place(x = 20, y = 237)

label_end_date_time = Label(ticket, text = 'End date time', font = ('B Titr', 10), bg = 'light blue')
label_end_date_time.place(x = 20, y = 277)

label_price = Label(ticket, text = 'Price', font = ('B Titr', 10), bg = 'light blue')
label_price.place(x = 20, y = 317)

label_seat_no = Label(ticket, text = 'Seat no', font = ('B Titr', 10), bg = 'light blue')
label_seat_no.place(x = 20, y = 357)

label_sold = Label(ticket, text = 'Sold', font = ('B Titr', 10), bg = 'light blue')
label_sold.place(x = 70, y = 437)

#Entry

entry_id = Entry(ticket, width = 30)
entry_id.place(x = 160, y = 42)

entry_ticket_code = Entry(ticket, width = 30)
entry_ticket_code.place(x = 160, y = 82)

src = StringVar()
entry_source = Entry(ticket, width = 30)
entry_source.place(x = 160, y = 122)

entry_destination = Entry(ticket, width = 30)
entry_destination.place(x = 160, y = 162)

entry_airline = Entry(ticket, width = 30)
entry_airline.place(x = 160, y = 202)

entry_start_date_time = Entry(ticket, width = 30, )
entry_start_date_time.place(x = 160, y = 242)

entry_end_date_time = Entry(ticket, width = 30)
entry_end_date_time.place(x = 160, y = 282)

entry_price = Entry(ticket, width = 30)
entry_price.place(x = 160, y = 322)

entry_seat_no = Entry(ticket, width = 30)
entry_seat_no.place(x = 160, y = 362)

#Checkbutton

checkbutton_sold = Checkbutton(ticket, onvalue = True, offvalue = False, bg = 'light blue')
checkbutton_sold.place(x = 120, y = 437)

#Button

btn_edit = Button(ticket, text = 'Edit', command = button_edit, width = 7, bg = 'dark gray', fg = 'white')
btn_remove = Button(ticket, text = 'Remove', command = button_remove, width = 7, bg = 'dark gray', fg = 'white')
btn_save = Button(ticket, text = 'Save', command = button_save, width = 20, bg = 'dark gray', fg = 'white')

btn_edit.place(x = 70, y = 500)
btn_remove.place(x = 160, y = 500)
btn_save.place(x = 70, y = 560)

#Table

table = ttk.Treeview(ticket, columns = ('id', 'ticket_code', 'source', 'destination', 'airline'), show = 'headings', height = 26)

table.heading('id', text = 'ID')
table.heading('ticket_code', text = 'Ticket code')
table.heading('source', text = 'Source')
table.heading('destination', text = 'Destination')
table.heading('airline', text = 'Airline')

table.column('id', width = 50)
table.column('ticket_code', width = 140)
table.column('source', width = 140)
table.column('destination', width = 140)
table.column('airline', width = 100)



table.place(x = 500, y = 40, width = 650)

ticket.mainloop()