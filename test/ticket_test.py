import re


end_time = "2025/05/23  23:30:00"
if not re.match(r"^\d{4}/\d{2}/\d{2} {2}\d{2}:\d{2}:\d{2}$", end_time):
    raise ValueError('Date is not valid')
else:
    print('saved successfully')