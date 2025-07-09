from datetime import datetime, timedelta
from model.entity.ticket import *

time_now = datetime.now()

def time_manage():
    if Ticket.start_date_time > time_now and time_now - Ticket.start_date_time >= timedelta(hours = 5):
        pass
    else:
        raise ValueError('Start date time is not valid !!!')

