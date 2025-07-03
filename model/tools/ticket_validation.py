import re
from datetime import datetime
from model.entity.ticket import Ticket


class TicketValidation:
    def ticket_validator_ticket_code(self, ticket):
        if not re.match(r"^[a-zA-Z/s]{5}$", ticket.ticket_code):
            raise ValueError("Name is not valid")

        def ticket_validator_origin(self, origin):
            if origin not in ["Tehran", "Isfahan", "Kerman", "Shiraz", "Tabriz", "Ahwaz", "Yazd", "Rasht", "Sari"]:
                raise ValueError("Origin is not valid")

        def ticket_validator_destination(self, destination):
            if destination not in ["Tehran", "Isfahan", "Kerman", "Shiraz", "Tabriz", "Ahwaz", "Yazd", "Rasht", "Sari"]:
                raise ValueError("Destination is not valid")

        def ticket_validator_airline(self, airline):
            if airline not in ["Mahan", "Aseman", "Iran Air", "Qeshm", "Kish AIR", "Caspian", "Zagros"]:
                raise ValueError("Airline is not valid")

        def ticket_validator_start_date_time(self, start_date):
            if start_date.time + 5 < datetime.now():
                raise ValueError("Start date is not valid")

        def ticket_validator_end_date_time(self, end_date):
            if end_date.time < ticket_validator_start_date_time():
                raise ValueError("End date is not valid")

        def ticket_validator_sold(self, status):
            if status == "Sold":
                pass

        def ticket_validator_code_search(self, ticket_code):
            if ticket_code in self.ticket_code:
                return self.ticket_code[ticket_code]

        def ticket_validator_origin_search(self, origin):
            if origin in ["Tehran", "Isfahan", "Kerman", "Shiraz", "Tabriz", "Ahwaz", "Yazd", "Rasht", "Sari"]:
                return origin.to_tuple_ticket()










