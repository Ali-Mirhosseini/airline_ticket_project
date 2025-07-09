import re
from datetime import datetime
from model.entity.ticket import *
from model.besiness_logic.ticket_bl import *


class TicketValidation:
    def ticket_code_validator(self, ticket):
        if not re.match(r"^[a-zA-Z0-9/s]{5}$", Ticket.ticket_code):
            raise ValueError("Name is not valid")

        def origin_validator(self, origin):
            if Ticket.origin not in ["Tehran", "Isfahan", "Kerman", "Shiraz", "Tabriz", "Ahwaz", "Yazd", "Rasht", "Sari", "Bandarabbas", "Arak", "Ardebil","Zanjan", "Kordestan"]:
                raise ValueError("Origin is not valid")

        def destination_validator(self, destination):
            if Ticket.destination not in ["Tehran", "Isfahan", "Kerman", "Shiraz", "Tabriz", "Ahwaz", "Yazd", "Rasht", "Sari", "Bandarabbas", "Arak", "Ardebil","Zanjan", "Kordestan"]:
                raise ValueError("Destination is not valid")

        def airline_validator(self, airline):
            if Ticket.airline not in ["Mahan", "Aseman", "Iran Air", "Qeshm", "Kish AIR", "Caspian", "Zagros"]:
                raise ValueError("Airline is not valid")

        def start_date_time_validator(self, start_date):
          
            time_manage()  
    #error
        
        def end_date_time_validator(self, end_time):
            
            if not re.match(r"^\d{4}/\d{2}/\d{2} {2}\d{2}:\d{2}:\d{2}$", Ticket.end_date_time):
                raise ValueError('Date is not valid')

        def sold_validator(self, status):
            if status == "Sold":
                pass

        def code_search_validator(self, ticket_code):
            if ticket_code in self.ticket_code:
                return self.ticket_code[ticket_code]

        def origin_search_validator(self, origin):
            if origin in ["Tehran", "Isfahan", "Kerman", "Shiraz", "Tabriz", "Ahwaz", "Yazd", "Rasht", "Sari"]:
                return origin.to_tuple_ticket()










