from model.tools.ticket_validation import *


ticket_list = []
class ticket_controller():
    
    def button_save(self, id, ticket_code, origin,
                 destination,
                 airline,
                 start_date_time,
                 end_date_time,
                 price,seat_number):
    
        try:
            ticket_ = Ticket(id, ticket_code, origin,
                    destination,
                    airline,
                    start_date_time,
                    end_date_time,
                    price,seat_number)
            ticket_list.append(ticket_)
            return True, f"Ticket Saved Successfully"
        except Exception as e:
            return False, f"Ticket Saved Failed\n{e}"
        
#        msg.showinfo(message = 'Saved Successfully')
#        print('saved successfully')