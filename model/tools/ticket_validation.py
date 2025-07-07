import re
from datetime import datetime
from model.entity.ticket import *


class TicketValidation:
    def ticket_code_validator(self, ticket):
        if not re.match(r"^[a-zA-Z0-9/s]{5}$", ticket.ticket_code):
            raise ValueError("Name is not valid")

        def origin_validator(self, origin):
            if origin not in ["Tehran", "Isfahan", "Kerman", "Shiraz", "Tabriz", "Ahwaz", "Yazd", "Rasht", "Sari", "Bandarabbas", "Arak", "Ardebil","Zanjan", "Kordestan"]:
                raise ValueError("Origin is not valid")

        def destination_validator(self, destination):
            if destination not in ["Tehran", "Isfahan", "Kerman", "Shiraz", "Tabriz", "Ahwaz", "Yazd", "Rasht", "Sari", "Bandarabbas", "Arak", "Ardebil","Zanjan", "Kordestan"]:
                raise ValueError("Destination is not valid")

        def airline_validator(self, airline):
            if airline not in ["Mahan", "Aseman", "Iran Air", "Qeshm", "Kish AIR", "Caspian", "Zagros"]:
                raise ValueError("Airline is not valid")

        def start_date_time_validator(self, start_date):
            pass

        def end_date_time_validator(self, end_date):
            pass

        def sold_validator(self, status):
            if status == "Sold":
                pass

        def code_search_validator(self, ticket_code):
            if ticket_code in self.ticket_code:
                return self.ticket_code[ticket_code]

        def origin_search_validator(self, origin):
            if origin in ["Tehran", "Isfahan", "Kerman", "Shiraz", "Tabriz", "Ahwaz", "Yazd", "Rasht", "Sari"]:
                return origin.to_tuple_ticket()










