from datetime import datetime

def is_today(date = datetime.today()): 
    return date == datetime.today()


print(is_today(datetime.today()))