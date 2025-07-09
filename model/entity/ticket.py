from model.tools.ticket_validation import *


class Ticket:
    def __init__(self,
                 id, 
                 ticket_code,
                 origin,
                 destination,
                 airline,
                 start_date_time,
                 end_date_time,
                 price,seat_number):
        
        
        self.id = id
        self.ticket_code = ticket_code
        self.origin = origin
        self.destination = destination
        self.airline = airline
        self.start_date_time = start_date_time
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.price = price
        self.seat_number = seat_number


    def to_tuple_ticket(self):
        return (self.id,
                self.ticket_code,
                self.origin,
                self.destination,
                self.airline,
                self.start_date_time,
                self.start_date_time,
                self.price, self.seat_number)


    @property
    def id(self):
        
        return self._id
    
    @id.setter
    def id(self, value):
        
        self._id = value
    
    @property
    def ticket_code(self):
        return self._ticket_code
    
    @ticket_code.setter
    def ticket_code(self, value):
        
        self._ticket_code = value
        
    @property
    def origin(self):
        return self._origin
    
    @origin.setter
    def origin(self, value):
        
        self._origin = value
    
    @property
    def destination(self):
        return self._destination
    
    @destination.setter
    def destination(self, value):
        
        self._destination = value
        
    @property
    def airline(self):
        return self._airline
    
    @airline.setter
    def airline(self, value):
        
        self._airline = value
        
    @property
    def start_date_time(self):
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self, value):
        
        self._start_date_time = value
        
    @property
    def end_date_time(self):
        return self._start_date_time
    
    @end_date_time.setter
    def end_date_time(self, value):
        
        self._end_date_time = value
        
    @property
    def end_date_time(self):
        return self._start_date_time
    
    @end_date_time.setter
    def end_date_time(self, value):
        
        self._end_date_time = value
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        
        self._price = value
        
    @property
    def seat_number(self):
        return self._seat_number
    
    @seat_number.setter
    def seat_number(self, value):
        
        self._seat_number = value