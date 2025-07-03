from model.tools.ticket_validation import TicketValidation


class Ticket:
    def __init__(self, id, ticket_code, origin, destination, airline, start_date_time, end_date_time, price,
                 seat_number):
        self.id = id
        self.ticket_code = ticket_code
        self.origin = origin
        self.destination = destination
        self.airline = airline
        self.start_date_time = start_date_time
        self.start_date_time = start_date_time
        self.price = price
        self.seat_number = seat_number

    def to_tuple_ticket(self):
        return (self.id, self.ticket_code, self.origin, self.destination, self.airline, self.start_date_time,
                self.start_date_time, self.price, self.seat_number)

    def validate(self):
        validator = TicketValidation()
        return validator.ticket_validator_ticket_code(self)

