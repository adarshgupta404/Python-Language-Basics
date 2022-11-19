from datetime import datetime

# datetime object containing current date and time

def time():
    '''code here'''
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string
print(time())